## Build with CMake

```sh
mkdir build
cd ../y2k38-checker/build
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=True \
    -DLLVM_DIR=../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/lib/cmake/llvm/ \
    ../clang-analyzer
make
```

## Running

単独実行プログラム、または、clang static analyzer plugin として実行できる。

````

### 単独実行プログラム

```sh
cd ../build
./bin/check-y2k38 -- ../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang -c ../dataset/blacklist/read-fs-timestamp.c
````

JSON Compilation Database を使用して実行することもできる。

```sh
cd ../build
./bin/check-y2k38 -p ../clang-analyzer/compile_commands.json
```

### Clang plugin

```sh
cd ../build
../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang -fplugin=lib/liby2k38-checker-plugin.so -c ../dataset/blacklist/read-fs-timestamp.c
```
