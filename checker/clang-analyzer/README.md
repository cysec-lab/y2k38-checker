## Build with CMake

### Preparation

LLVM 11.0.0 の展開
https://github.com/llvm/llvm-project/releases/tag/llvmorg-11.0.0

```sh
cd ./checker/clang-analyzer
curl -L https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz | tar -Jxf -
```

### Build

```sh
mkdir build
cd ../y2k38-checker/build
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=True \
    -DLLVM_DIR=../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/lib/cmake/llvm/ \
    ../clang-analyzer
make
```

## Run

単独実行プログラム、または、clang static analyzer plugin として実行できる。

### Run as a standalone tool

```sh
cd ../build
./bin/check-y2k38 -- ../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang -c ../dataset/blacklist/read-fs-timestamp.c
```

JSON Compilation Database を使用して実行することもできる。
この場合、カレントディレクトリは `clang-analyzer/build/` でなくても可。

```sh
pwd # path/to/repo
./build/bin/check-y2k38 -p ./clang-analyzer/compile_commands.json
```

### Run as a Clang plugin

```sh
cd ../build
../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang \
        -fplugin=lib/libread-fs-timestamp-plugin.so \
    -c ../dataset/blacklist/write-fs-timestamp.c
```

※ `-fplugin`は一つしか指定できない。

```
        -fplugin=lib/libwrite-fs-timestamp-plugin.so \
        -fplugin=lib/libtimet-to-int-downcast-plugin.so \
        -fplugin=lib/libtimet-to-long-downcast-plugin.so \
```
