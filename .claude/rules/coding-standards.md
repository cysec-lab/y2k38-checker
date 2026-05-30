# Coding Standards

## Rust (`checker/reporter/`)

### Formatting & Linting

- All code must be formatted with `rustfmt` (run `just fmt-rust` or `cargo fmt`).
- All code must pass `cargo clippy -- -D warnings`. New `#[allow(clippy::...)]` requires a
  comment explaining why.
- Zero warnings policy: `RUSTFLAGS="-D warnings"` is the target.

### Naming

| Item | Convention | Example |
|------|-----------|---------|
| Types, traits, enums | `PascalCase` | `Y2k38Category`, `Y2k38Checker` |
| Functions, methods, variables | `snake_case` | `parse_clang_output` |
| Constants | `SCREAMING_SNAKE_CASE` | `CLANG_PATH`, `PLUGIN_PATH` |
| Modules | `snake_case` | `analysis_workflow_executor` |
| Enum variants | `PascalCase` | `ReadFsTimestamp`, `TimetToIntDowncast` |

### Code Organization

- Public items first, then private.
- `#[cfg(test)]` test modules at the bottom of each file.
- Group related functions; do not scatter helpers.

### Abstractions

- Introduce a trait only when there are multiple implementations or testability requires it.
  (`Y2k38Checker` trait exists because `ClangPluginY2k38Checker` needs a mock for unit tests.)
- Prefer concrete types. Three similar functions are better than a premature generic.

### Error Handling

See `.claude/rules/error-handling.md` for full guidelines.

- Use `Result<T, E>` for fallible operations; never `unwrap()` in non-test code.
- Propagate errors with `?`; add context with `.map_err(|e| ...)` at boundaries.

### Regex

Compile `Regex` at most once per pattern. Patterns called in loops must use `once_cell` or
be pre-compiled:

```rust
use once_cell::sync::Lazy;
static RE: Lazy<Regex> = Lazy::new(|| Regex::new(r"...").unwrap());
```

### Comments

Write comments only when the *why* is non-obvious. Do not narrate what the code does.

## C++ (`checker/clang-analyzer/`)

- Build flags enforce `-fno-rtti -Wall`; do not introduce RTTI-dependent patterns.
- Follow Clang plugin conventions: one `ASTFrontendAction` subclass per check.
- Use Clang's `DiagnosticsEngine` for all output — never `fprintf`/`std::cerr`.
- No raw owning pointers; use `std::unique_ptr` or Clang allocator.

## Python (`checker/script/`)

- Format with `ruff format`; lint with `ruff check`.
- Use `pathlib.Path` for all file operations; no string concatenation for paths.
- All public functions get a one-line docstring.
- Tests use `unittest`; test files named `test_*.py`.
