# fs-y2k38-checker based on clang-query

## 実行

```sh
sh ./fs-y2k38-checker.sh <file>.c
```

```sh
alias fs-y2k38-checker="sh /home/cysec/Develop/fsyc/fs-y2k38-checker/clang-query/fs-y2k38-checker.sh"
```

## Matcher

### キャスト式

明示的な型キャスト

```sh
cStyleCastExpr()
```

暗黙的な型キャスト > 代入演算

```sh
varDecl(
    has(implicitCastExpr())
)
```

暗黙的な型キャスト > 関数呼び出し式の引数

```sh

callExpr(
    hasAnyArgument(implicitCastExpr())
)
```

暗黙的な型キャスト > return 文

```sh
returnStmt(
    hasReturnValue(implicitCastExpr())
)
```

### キャスト後 条件

```sh
hasType(asString("int"))
```

### キャスト元 条件

```sh
has(anyOf(
    expr(
        unless(binaryOperator()),   # 二項演算以外の式
        anyOf(                      # time_t 型
            hasType(asString("time_t")),
            hasType(asString("__time_t"))
        )
    ),
    binaryOperator(                 # 二項演算 式
        hasType(asString("long")),  # long 型
        hasDescendant(anyOf(        # 子孫に指定のノードをもつ
            callExpr(               # time_t 型の呼び出し式で、引数に time_t 型の式をもたない
                unless(hasAnyArgument(expr(anyOf(
                    hasType(asString("time_t")),
                    hasType(asString("__time_t"))
                )))),
                anyOf(
                    hasType(asString("time_t")),
                    hasType(asString("__time_t"))
                )
            ),
            expr(                   # 呼び出し式でない time_t 型の式で、先祖に呼び出し式をもたない
                unless(hasAncestor(callExpr())),
                anyOf(
                    hasType(asString("time_t")),
                    hasType(asString("__time_t"))
                )
            )
        ))
    )
))
```
