root          := justfile_directory()
checker_dir   := root / "checker"
reporter_dir  := checker_dir / "reporter"
build_dir     := checker_dir / "build"
llvm_name     := "clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04"
llvm_dir      := checker_dir / llvm_name
llvm_cmake    := llvm_dir / "lib/cmake/llvm"
llvm_url      := "https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/" + llvm_name + ".tar.xz"
llvm_sha256   := "829f5fb0ebda1d8716464394f97d5475d465ddc7bea2879c0601316b611ff6db"

default:
    @just --list

# ── Setup ──────────────────────────────────────────────────────────────────

# First-time devbox setup: download LLVM 11 + build everything
setup-dev: setup-llvm build

# Download LLVM 11 (required for building the Clang plugin)
setup-llvm:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ -d "{{llvm_dir}}" ]; then
        echo "LLVM 11 already present at {{llvm_dir}}"
        exit 0
    fi
    cd "{{checker_dir}}"
    tarball="{{llvm_name}}.tar.xz"
    # Remove the tarball on exit (success or failure) so a bad/partial
    # download never lingers; the extracted dir is what we keep.
    trap 'rm -f "$tarball"' EXIT
    echo "Downloading LLVM 11 (~700 MB)..."
    curl -fL --retry 5 --retry-delay 2 --retry-connrefused -o "$tarball" "{{llvm_url}}"
    echo "Verifying checksum..."
    echo "{{llvm_sha256}}  $tarball" | sha256sum -c -
    echo "Extracting..."
    tar -Jxf "$tarball"
    echo "Done."

# ── Build ──────────────────────────────────────────────────────────────────

# Build everything (Clang plugin + Rust reporter)
build: build-plugin build-reporter

# Build the Clang plugin (requires LLVM 11; run `just setup-llvm` first)
build-plugin:
    mkdir -p "{{build_dir}}"
    cd "{{build_dir}}" && cmake \
        -DCMAKE_EXPORT_COMPILE_COMMANDS=True \
        -DLLVM_DIR="{{llvm_cmake}}" \
        -DCMAKE_BUILD_RPATH="{{llvm_dir}}/lib" \
        "{{checker_dir}}/clang-analyzer"
    cd "{{build_dir}}" && make -j$(nproc)

# Build the Rust reporter
build-reporter:
    cd "{{reporter_dir}}" && cargo build --release

# ── Format ─────────────────────────────────────────────────────────────────

# Format all code in-place
fmt:
    cd "{{reporter_dir}}" && cargo fmt

# Check formatting + lint without modifying (used by CI)
fmt-check:
    cd "{{reporter_dir}}" && cargo fmt -- --check
    cd "{{reporter_dir}}" && cargo clippy -- -D warnings

# ── Test ───────────────────────────────────────────────────────────────────

# Run only tests that do NOT require LLVM/plugin (used by CI `test` job).
# Integration tests are marked `#[ignore]` and are skipped by plain `cargo test`.
test-unit:
    cd "{{reporter_dir}}" && cargo test

# Run ONLY the ignored integration tests (requires LLVM 11 + built plugin)
test-integration:
    cd "{{reporter_dir}}" && cargo test -- --ignored

# Run ALL tests incl. integration (requires LLVM 11 + built plugin)
test:
    cd "{{reporter_dir}}" && cargo test -- --include-ignored

# ── Run ────────────────────────────────────────────────────────────────────

# Run the checker against a C source file
check FILE:
    cd "{{reporter_dir}}" && cargo run --release -- "{{FILE}}"

# ── CI (local simulation) ──────────────────────────────────────────────────

# Full CI suite locally (requires `just setup-llvm` first)
ci: fmt-check build test

# Fast CI suite (no LLVM): exactly what the `fmt` + `test` CI jobs run
ci-fast: fmt-check test-unit
