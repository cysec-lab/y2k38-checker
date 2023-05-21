## Build with CMake

```sh
mkdir build
cd ../y2k38-checker/build
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=True \
    -DLLVM_DIR=../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/lib/cmake/llvm/ \
    ../clang-analyzer
make
```

## 実行

単独実行プログラム、または、clang static analyzer plugin として実行できる。

### 単独ツールとして実行

```sh
cd ../build
./bin/check-y2k38 -- ../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang -c ../dataset/blacklist/read-fs-timestamp.c
```

JSON Compilation Database を使用して実行することもできる。
この場合、カレントディレクトリは `clang-analyzer/build/` でなくても可。

```sh
pwd # path/to/repo
./build/bin/check-y2k38 \
    -p ./clang-analyzer/compile_commands.json \
    -y2k38-checker-output ~/develop/y2k38-checker/clang-analyzer/analyzed.json
```

### Clang plugin として実行

```sh
cd ../build
../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang \
        -fplugin=lib/libread-fs-timestamp-plugin.so \
        -fplugin=lib/libwrite-fs-timestamp-plugin.so \
        -fplugin=lib/libtimet-to-int-downcast-plugin.so \
        -fplugin=lib/libtimet-to-long-downcast-plugin.so \
    -c ../dataset/blacklist/write-fs-timestamp.c
```
