# y2k38-checker

[Paper](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=228078&item_no=1&page_id=13&block_id=8)

y2k38-checker is a tool that identifies and reports code with potential Year 2038 problem issues in C language source code.


## Check List

| Check list ID | Description |
| --- | --- |
| read-fs-timestamp | Since the file timestamp attributes of ext2/3, XFS (versions prior to Linux 5.10), ReiserFS are 32-bit signed integers, programs that read file timestamps in these environments may be affected by the Y2K38. |
| write-fs-timestamp | Since the file timestamp attributes of ext2/3, XFS (versions prior to Linux 5.10), ReiserFS are 32-bit signed integers, programs that write file timestamps in these environments may be affected by the Y2K38. |
| timet-to-int-downcast | Since in many environments the int type is a 32-bit signed integer, there is a possibility that downcasting from `time_t` type to `int` may be affected by the Y2K38. |
| timet-to-long-downcast | Since in many environments the int type is a 32-bit signed integer, there is a possibility that downcasting from `time_t` to `long` may be affected by the Y2K38. |

## Pre-built detection tool

See [Releases](https://github.com/cysec-lab/y2k38-checker/releases/) to download and run the pre-built detection tool.

- Prerequisites: Docker/Docker Compose are installed.

## Preparation

1. Clone the repository
   ```sh
   git clone https://github.com/cysec-lab/y2k38-checker.git
   ```
2. Create the directory for the detecting target source code, and add files to be analyzed. 
   ```sh
   mkdir <path/to/dir>
   cp -r <files/to/be/analyzed> <path/to/dir>
   ``` 

3. Add the path of the created the directory in `.devcontainer/docker-compose.yml`
   ```diff
   services:
      y2k38-checker-app:
         build:
            context: ..
            dockerfile: .devcontainer/Dockerfile
         tty: true
         volumes:
            - ..:/root/y2k38-checker
            - type: bind
   -          source: /home/cysec/develop/.y2k38-checker/analysis-objects/
   +          source: <path/to/dir>
            target: /root/analysis-objects
   ```

3. Build & Run the docker container with CLI or DevContainer
   ```sh
   cd y2k38-checker
   docker-compose build # only first time
   docker-compose run y2k38-checker 
   ```
   Alternatively, start it in the devcontainer of VSCode.
   

## How to build

1. Move to the checker/ directory
   ```sh
   cd ./checker/clang-analyzer
   ```
2. Downlaod LLVM library

   ```sh
   curl -L https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz | tar -Jxf -
   ```
   - https://github.com/llvm/llvm-project/releases/tag/llvmorg-11.0.0

3. Build with CMake
   ```sh
   mkdir build
   cd ../y2k38-checker/build
   cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=True \
      -DLLVM_DIR=../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/lib/cmake/llvm/ \
      ../clang-analyzer
   make
   ```

## How to Run

It can be executed as a standalone program or as a clang static analyzer plugin.

### Simple example

```sh
pwd # y2k38-checker/
python3 ./checker/run.py -input=dataset/**/*.c -output=example/results.json
```

### Run as a standalone tool

```sh
cd ../build
./bin/check-y2k38 -- ../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang -c ../../dataset/blacklist/read-fs-timestamp.c
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

> [!NOTE]  
> Only one -fplugin option can be specified.

| Check list ID | plugin path | 
| --- | --- |
| read-fs-timestamp | {repo}/checker/build/lib/libread-fs-timestamp-plugin.so |
| write-fs-timestamp | {repo}/checker/build/lib/libwrite-fs-timestamp-plugin.so |
| timet-to-int-downcast | {repo}/checker/build/lib/libtimet-to-int-downcast-plugin.so |
| timet-to-long-downcast | {repo}/checker/build/lib/libtimet-to-long-downcast-plugin.so |

# License

TODO

