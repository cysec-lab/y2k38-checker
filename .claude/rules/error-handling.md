# Error Handling (Rust)

## Core Rules

**Use `Result<T, E>` for all fallible operations.** Never `unwrap()` or `expect()` in non-test
code paths that could receive unexpected input.

```rust
// CORRECT
fn run_clang(file: &File) -> Result<String, io::Error> { ... }

// WRONG (panics in production)
let output = run_clang(file).unwrap();
```

**Propagate with `?`** at the call site; add context at boundaries:

```rust
fn analyze(file: &File) -> Result<Vec<AnalysisDetail>, AnalysisError> {
    let raw = run_clang_process(file)
        .map_err(|e| AnalysisError::ClangFailed { path: file.path().into(), source: e })?;
    Ok(parse_clang_output(&raw))
}
```

## Error Context

Add context when crossing module/layer boundaries. The error message should answer
"what were we trying to do?" not just "what went wrong?":

```rust
// GOOD
.map_err(|e| format!("failed to run clang on {}: {}", file.path(), e))

// BAD — no context about which file or operation
.map_err(|e| e.to_string())
```

## Silent Discard

Never discard errors silently. If ignoring intentionally, add a comment:

```rust
let _ = cleanup_temp_file(path); // best-effort cleanup, failure is non-fatal
```

## Panics

Reserve `panic!` / `unwrap()` / `expect()` for:
- `#[cfg(test)]` code
- Programmer errors that indicate a bug (e.g., invariant violation that should never happen)
- One-time startup initialization where recovery is impossible

```rust
// OK in tests
assert!(result.is_ok());

// OK for a Regex that is a compile-time constant
static RE: Lazy<Regex> = Lazy::new(|| Regex::new(r"...").unwrap());
```

## Current Tech Debt

`run_clang_process()` returns `io::Error` directly. Long-term, introduce a typed error enum
(e.g., with `thiserror`) to distinguish:
- Clang binary not found (`io::ErrorKind::NotFound`)
- Non-zero exit code (plugin diagnostic)
- UTF-8 decode failure

Until that refactor, add context in callers when surfacing errors to the user.
