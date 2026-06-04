# CLAUDE.md

## Worktree Isolation (MUST READ FIRST)

**ALWAYS call `EnterWorktree` before doing any work that changes files.** This prevents branch
conflicts when multiple sessions run in parallel. Give it a descriptive name (e.g.,
`feat-timet-downcast`). Commit before exiting and tell the user the branch name.

**Worktree deletion is dangerous — other sessions may depend on it.** NEVER remove a locked or
unmerged worktree. See `.claude/rules/git-workflow.md` for the full safe cleanup protocol.

## Build & Test

```bash
# First-time setup (downloads ~700 MB LLVM 11)
just setup-llvm

# First-time setup + build in one step (preflight → setup-llvm → build)
just setup-dev      # `devbox run setup` is a thin wrapper around this

# Build everything
just build          # Clang plugin (cmake) + Rust reporter (cargo)
just build-plugin   # Clang plugin only
just build-reporter # Rust reporter only

# Format
just fmt            # format in-place
just fmt-check      # CI: check without modifying

# Test
just test-unit         # unit tests — no LLVM/plugin required
just test-integration  # integration tests only (#[ignore]'d; needs LLVM + plugin)
just test              # everything incl. integration (needs setup-llvm + build)

# Run the checker
just check path/to/file.c

# CI suites (each CI job runs the matching recipe — local == CI)
just ci-fast        # fmt-check + test-unit (no LLVM; mirrors the fmt + test CI jobs)
just ci             # full suite: fmt-check + build + test
```

> Integration tests are annotated `#[ignore]` because they shell out to the
> real Clang plugin (LLVM 11 + a built plugin). Default clang/plugin/dataset
> paths are derived from the crate location (`CARGO_MANIFEST_DIR`), so they
> run from any checkout; override clang/plugin with `CLANG_PATH` / `PLUGIN_PATH`.
> Plain `cargo test` (and `just test-unit`) skips them; `cargo test -- --ignored`
> (or `just test-integration`) runs only those.

## Architecture

Two components work together:

1. **Clang plugin** (`checker/clang-analyzer/`) — C++ AST visitors that emit `y2k38 (<category>)`
   warnings via Clang's diagnostic system. Built to `checker/build/lib/liby2k38-plugin.so`.

2. **Rust reporter** (`checker/reporter/`) — Orchestrates analysis, shells out to clang with the
   plugin loaded, parses stderr, and outputs structured results.

See `docs/spec.md` for full architecture, data flow, and check list specification.

## Check Categories

| ID | Description |
|----|-------------|
| `read-fs-timestamp` | Reading 32-bit filesystem timestamps (ext2/3, XFS <5.10, ReiserFS) |
| `write-fs-timestamp` | Writing 32-bit filesystem timestamps |
| `timet-to-int-downcast` | Casting `time_t` → `int` |
| `timet-to-long-downcast` | Casting `time_t` → `long` |

## Platform Constraint

The Clang plugin is **Linux x86_64 only** (pre-built LLVM 11 for `ubuntu-20.04`). macOS and
Windows are not supported.

## Dev Environment (devbox)

[devbox](https://www.jetify.com/devbox) provides a reproducible local toolchain (cmake, gcc,
rustup, just, etc.) from nixpkgs. LLVM 11 itself still comes from the tarball via
`just setup-llvm`.

```bash
devbox shell           # enter the environment (installs Nix + packages on first run)
devbox run setup       # thin wrapper around `just setup-dev` (preflight → setup-llvm → build)
just ci-fast           # fmt-check + test-unit
```

`devbox.lock` pins exact package versions, so the environment is identical across machines.

## CI

GitHub Actions (`.github/workflows/ci.yml`) runs four jobs, each invoking the matching `just`
recipe so that **"passes locally" implies "passes in CI"**:

| Job | Recipe | Notes |
|-----|--------|-------|
| Format & Lint | `just fmt-check` | rustfmt + clippy (`-D warnings`) |
| Test | `just test-unit` | Rust unit tests; no LLVM required |
| Build | `just setup-llvm` + `just build` | Clang plugin + Rust reporter; LLVM 11 cached |
| E2E | `just test-integration` | Real plugin e2e tests only; required gate (paths derived from `CARGO_MANIFEST_DIR`) |

Reproduce the fast jobs locally with `just ci-fast`.

## Agents

Specialized agents live in `.claude/agents/`:

- **code-reviewer** — correctness/safety/consistency review before a PR
- **planner** — design the approach before adding a new check or feature
- **refactor-cleaner** — find and safely remove dead code

## Rules & Docs

- Git workflow: `.claude/rules/git-workflow.md`
- Security: `.claude/rules/security.md`
- Coding standards (Rust): `.claude/rules/coding-standards.md`
- Error handling (Rust): `.claude/rules/error-handling.md`
- Test design: `.claude/rules/test-design.md`
