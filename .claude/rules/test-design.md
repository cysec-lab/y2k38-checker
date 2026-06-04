# Test Design

## Core Principles

- **Equivalence partitioning**: divide input domain into classes that behave identically; test one
  representative per class.
- **Boundary value analysis**: test edge cases where bugs cluster (empty input, single line,
  malformed output).
- **Error guessing**: attack likely failure points in parsers (e.g., `parse_clang_output` with
  truncated lines, non-UTF8 bytes, multiple warnings on the same line).

## Test Pyramid

```
Unit tests (fast, no I/O)        ← most tests live here
  └─ Integration tests (clang subprocess)
      └─ Dataset smoke tests (blacklist/whitelist)
```

## Rust Tests

### Unit tests (no LLVM required)

Place in `#[cfg(test)]` module at the bottom of the source file. Use `Y2k38CheckerMock` to
isolate Rust logic from the Clang subprocess:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use crate::y2k38_checker::y2k38_checker_mock::Y2k38CheckerMock;

    #[test]
    fn parse_empty_output_returns_empty_vec() {
        assert_eq!(parse_clang_output(""), vec![]);
    }

    #[test]
    fn parse_single_warning_extracts_all_fields() {
        let line = "foo.c:3:11: warning: y2k38 (read-fs-timestamp): desc\n";
        let details = parse_clang_output(line);
        assert_eq!(details.len(), 1);
        assert_eq!(details[0].y2k38_category(), &Y2k38Category::ReadFsTimestamp);
        assert_eq!(details[0].row(), 3);
        assert_eq!(details[0].column(), 11);
    }
}
```

### Integration tests (require LLVM + plugin)

Mark tests that invoke the real Clang subprocess with a comment `// integration test` and group
them separately. They must not be the *only* tests for a unit of logic.

### AAA Structure

Every test follows **Arrange / Act / Assert**:

```rust
#[test]
fn test_name() {
    // Arrange
    let input = ...;

    // Act
    let result = function_under_test(input);

    // Assert
    assert_eq!(result, expected);
}
```

## Dataset Tests

`dataset/blacklist/` — each file MUST produce at least one warning for its named check.
`dataset/whitelist/` — each file MUST produce zero warnings.

When adding a new check, add both a blacklist and a whitelist file. Naming convention:
`<check-id>.c` (e.g., `timet-to-int-downcast.c`).

## What NOT to Test

- Do not test Clang's AST parsing — trust the compiler.
- Do not test `std::process::Command` behavior — it's stdlib.
- Do not write tests that only verify that a struct field can be read back.
