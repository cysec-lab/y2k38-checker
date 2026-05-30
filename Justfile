root          := justfile_directory()
checker_dir   := root / "checker"
reporter_dir  := checker_dir / "reporter"
build_dir     := checker_dir / "build"
script_dir    := checker_dir / "script"
llvm_name     := "clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04"
llvm_dir      := checker_dir / llvm_name
llvm_cmake    := llvm_dir / "lib/cmake/llvm"

default:
    @just --list

# ── Setup ──────────────────────────────────────────────────────────────────

# Download LLVM 11 (required for building the Clang plugin)
setup-llvm:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ -d "{{llvm_dir}}" ]; then
        echo "LLVM 11 already present at {{llvm_dir}}"
        exit 0
    fi
    echo "Downloading LLVM 11 (~700 MB)..."
    cd "{{checker_dir}}" && curl -L \
        "https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/{{llvm_name}}.tar.xz" \
        | tar -Jxf -
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
        "{{checker_dir}}/clang-analyzer"
    cd "{{build_dir}}" && make -j$(nproc)

# Build the Rust reporter
build-reporter:
    cd "{{reporter_dir}}" && cargo build --release

# ── Format ─────────────────────────────────────────────────────────────────

# Format all code in-place
fmt: fmt-rust fmt-python

fmt-rust:
    cd "{{reporter_dir}}" && cargo fmt

fmt-python:
    ruff format "{{script_dir}}"

# Check formatting without modifying (used by CI)
fmt-check: fmt-check-rust fmt-check-python

fmt-check-rust:
    cd "{{reporter_dir}}" && cargo fmt -- --check
    cd "{{reporter_dir}}" && cargo clippy -- -D warnings

fmt-check-python:
    ruff check "{{script_dir}}"

# ── Test ───────────────────────────────────────────────────────────────────

# Run all tests (requires built Clang plugin)
test: test-rust test-python

# Run only unit tests that do not require LLVM/plugin
test-unit:
    cd "{{reporter_dir}}" && cargo test test_parse_clang_output test_to_y2k38_category_enum

# Run all Rust tests (requires LLVM 11 + built plugin at hardcoded Docker paths)
test-rust:
    cd "{{reporter_dir}}" && cargo test

# Run Python unit tests
test-python:
    cd "{{script_dir}}/analyze" && PYTHONPATH=$(pwd) python3 -m unittest discover

# ── Run ────────────────────────────────────────────────────────────────────

# Run the checker against a C source file
check FILE:
    cd "{{reporter_dir}}" && cargo run --release -- "{{FILE}}"

# ── CI (local simulation) ──────────────────────────────────────────────────

# Run the full CI suite locally
ci: fmt-check build test
