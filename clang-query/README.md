# clang-query

## read 系 バグ

```sh
cd read-bug/
clang-query -f read-bug.matcher read-bug.c --
```

## ダウンキャスト バグ

```sh
cd downcast-bug/
clang-query -f exp-downcast-bug.matcher exp-downcast-bug.c --
clang-query -f assign-imp-downcast.matcher assign-imp-downcast.c --
clang-query -f return-imp-downcast.matcher return-imp-downcast.c --
clang-query -f func-arg-imp-downcast.matcher func-arg-imp-downcast.c --
```

## write 系 バグ

```sh
cd write-bug/
clang-query -f write-bug.matcher write-bug.c --
```
