# clang-query

## read 系 バグ

```sh
clang-query -f match-read-bug test.c --
```

## 明示的ダウンキャスト バグ

```sh
clang-query -f match-exp-downcast-bug test.c --
```

## 暗黙的ダウンキャスト バグ

```sh
clang-query -f match-imp-downcast-bug test.c --
```

## write 系 バグ

```sh
clang-query -f match-write-bug test.c --
```
