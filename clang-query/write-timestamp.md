## Matcher

`utime()` または `utimes()` にマッチする Matcher

```
declRefExpr(to(
    functionDecl(
        anyOf(
            hasName("utime"),
            hasName("utimes")
        )
    )
))
```

## clang-query

```
set traversal     IgnoreUnlessSpelledInSource
set bind-root     true
set print-matcher true
enable output     dump

m declRefExpr(to(functionDecl(anyOf(hasName("utime"),hasName("utimes")))))
```
