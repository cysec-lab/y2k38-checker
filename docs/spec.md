# y2k38-checker Specification

## Overview

y2k38-checker is a static analysis tool that detects C source code patterns susceptible to the
Year 2038 problem (Y2K38). The Y2K38 problem occurs when a 32-bit signed integer is used to
represent a Unix timestamp: the maximum representable value is `2^31 - 1 = 2147483647`,
corresponding to 2038-01-19 03:14:07 UTC.

Reference: [IPSJ Paper](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=228078&item_no=1&page_id=13&block_id=8)

---

## Architecture

```
y2k38-checker/
├── checker/
│   ├── clang-analyzer/        # C++ Clang plugin (detection engine)
│   │   ├── lib/               # Per-check AST action implementations
│   │   └── tools/             # Standalone check-y2k38 binary (legacy)
│   ├── build/                 # CMake build output
│   │   └── lib/liby2k38-plugin.so  # Compiled Clang plugin
│   └── reporter/              # Rust binary (orchestrator + reporter)
│       └── src/
│           ├── main.rs
│           ├── analyzer/      # AnalysisWorkflowExecutor, Timer
│           ├── y2k38_checker/ # Checker trait + ClangPlugin impl + Mock
│           └── domain/        # Value objects: File, AnalysisDetail, Y2k38Category
└── dataset/                   # Sample C files (blacklist = should trigger, whitelist = should not)
```

### Data Flow

```
Input: C source file path
  │
  ▼
[Rust: AnalysisWorkflowExecutor]
  │  spawns subprocess
  ▼
[clang -fplugin=liby2k38-plugin.so -c <file>]
  │  writes warnings to stderr
  ▼
[Rust: parse_clang_output()]
  │  regex: "file:row:col: warning: y2k38 (<category>)"
  ▼
Output: Vec<AnalysisDetail> { category, file, row, column }
```

---

## Check List

### `read-fs-timestamp`

**Trigger**: Reading file timestamp attributes (`st_atime`, `st_mtime`, `st_ctime`) from `struct stat`.

**Risk**: On ext2/3, XFS (< Linux 5.10), and ReiserFS, these fields are stored as 32-bit signed
integers. Programs that read and process these values may produce incorrect results after
2038-01-19.

**Detection**: Clang AST visitor identifies member expressions accessing timestamp fields of `stat`.

---

### `write-fs-timestamp`

**Trigger**: Writing to file timestamp attributes via `utimes(2)`, `utimensat(2)`, or direct
`struct stat` field assignment.

**Risk**: Same filesystem constraint as `read-fs-timestamp`. Writes that compute future timestamps
will silently overflow on affected filesystems.

**Detection**: Clang AST visitor identifies assignments to timestamp fields of `stat`.

---

### `timet-to-int-downcast`

**Trigger**: Implicit or explicit cast from `time_t` to `int`.

**Risk**: On most platforms `int` is a 32-bit signed integer. Downcasting `time_t` (which is
64-bit on modern 64-bit systems) to `int` will overflow after 2038-01-19.

**Detection**: Clang AST visitor identifies `ImplicitCastExpr` and `CStyleCastExpr` nodes that
narrow `time_t` to `int`.

---

### `timet-to-long-downcast`

**Trigger**: Implicit or explicit cast from `time_t` to `long`.

**Risk**: On 32-bit platforms and Windows, `long` is a 32-bit signed integer. Downcasting to
`long` is not universally safe.

**Detection**: Same mechanism as `timet-to-int-downcast`, targeting `long`.

---

## Components

### Clang Plugin (`clang-analyzer/`)

Built with CMake against LLVM/Clang 11. Produces `liby2k38-plugin.so`.

Each check is an independent `ASTFrontendAction` subclass registered under a common plugin entry
point (`y2k38-all`). New checks are added by:

1. Creating `lib/<check-name>/` with `*Action.{h,cpp}` (use `y2k38::MatcherCallback<T>` and `y2k38::ActionBase<D>` from `Y2k38CheckBase.h`).
2. Adding the action to `Y2k38AllAction`.
3. Adding a one-line `CMakeLists.txt` that calls `add_y2k38_check(<name> <source>)`.

### Rust Reporter (`reporter/`)

Orchestrates analysis runs, parses Clang stderr output, and formats results.

Key types:
- `Y2k38Checker` trait — abstraction over the Clang plugin (enables mock testing)
- `ClangPluginY2k38Checker` — concrete impl that shells out to clang
- `AnalysisWorkflowExecutor` — iterates files, collects `AnalysisDetail` results
- `AnalysisDetail` — `(Y2k38Category, File, row: u32, column: u32)`

Environment variables (override defaults at runtime):
- `CLANG_PATH` — clang binary (default: bundled LLVM 11)
- `PLUGIN_PATH` — plugin `.so` (default: `checker/build/lib/liby2k38-plugin.so`)

### Dataset (`dataset/`)

```
dataset/
├── blacklist/   # C files that MUST trigger at least one warning
└── whitelist/   # C files that MUST trigger zero warnings
```

Used for regression testing.

---

## Build Requirements

| Component | Requirement |
|-----------|-------------|
| Clang plugin | LLVM/Clang 11, CMake ≥ 3.12, C++14 compiler |
| Rust reporter | Rust ≥ 1.65 (edition 2021) |
| Formatting | `rustfmt`, `cargo clippy` |

Download LLVM 11: `just setup-llvm` (see `Justfile`)

---

## Testing Strategy

### Unit tests (no LLVM required)
- `test_parse_clang_output` — verifies regex parsing of Clang stderr
- `test_to_y2k38_category_enum` — verifies string-to-enum mapping

### Integration tests (require LLVM + built plugin)

These are annotated `#[ignore]` so a plain `cargo test` skips them. They shell out to the real
Clang plugin via the hardcoded `/root/y2k38-checker` paths (known tech debt).

- `test_run_clang_process` — invokes real clang subprocess
- `test_health_check` — verifies clang binary is reachable
- `test_run` (checker + executor) — end-to-end with dataset files

### Running tests

| Command | Scope |
|---------|-------|
| `just test-unit` | Unit tests (Rust + Python); no LLVM required |
| `just test-integration` | `#[ignore]`'d integration tests only (`cargo test -- --ignored`) |
| `just test` | Everything, incl. integration (inside Docker / after `just setup-llvm` + `just build`) |
