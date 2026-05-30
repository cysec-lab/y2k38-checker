# y2k38-checker

[Paper](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=228078&item_no=1&page_id=13&block_id=8)

y2k38-checker is a tool that identifies and reports code with potential Year 2038 problem issues in C language source code.

## Check List

| Check list ID          | Description                                                                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| read-fs-timestamp      | Since the file timestamp attributes of ext2/3, XFS (versions prior to Linux 5.10), ReiserFS are 32-bit signed integers, programs that read file timestamps in these environments may be affected by the Y2K38.  |
| write-fs-timestamp     | Since the file timestamp attributes of ext2/3, XFS (versions prior to Linux 5.10), ReiserFS are 32-bit signed integers, programs that write file timestamps in these environments may be affected by the Y2K38. |
| timet-to-int-downcast  | Since in many environments the int type is a 32-bit signed integer, there is a possibility that downcasting from `time_t` type to `int` may be affected by the Y2K38.                                           |
| timet-to-long-downcast | Since in many environments the int type is a 32-bit signed integer, there is a possibility that downcasting from `time_t` to `long` may be affected by the Y2K38.                                               |

## How to use

Requirements:

- Docker / Docker Compose
- OS: Ubuntu

### Setup

1. Download the [releases](https://github.com/cysec-lab/y2k38-checker/releases/).
2. Unzip the downloaded file.

```sh
unzip y2k38-checker-<version>.zip
```

Then, the following directory structure is created.

```ini
y2k38-checker/
├─┬ checker/
│  ├── build/lib/liby2k38-plugin.so  # detection tool as a Clang plugin
│  ├── reporter/                      # Rust CLI runner
│  └── clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04
├── dataset/             # example for C source code
├── volumes/             # target source code
└┬─ .devcontainer/
  ├── Dockerfile
  ├── docker-compose.yml
  └── devcontainer.json
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
         - ..:/root/y2k38-checker/volumes/
         - type: bind
-          source: /home/cysec/develop/.y2k38-checker/analysis-objects/
+          source: <path/to/dir>
         target: /root/analysis-objects
```

4. Build & Run the docker container with CLI or DevContainer

```sh
cd y2k38-checker
docker-compose build # only first time
docker-compose run y2k38-checker
```

Alternatively, start it in the devcontainer of VSCode.

5. Run the detection tool with the following command.

### Run

Check the source code in the `volumes/` directory with the detection tool.

```sh
cd checker/reporter
cargo run -- <file.c>
# cargo run -- ../../dataset/blacklist/read-fs-timestamp.c
```

The Clang binary and plugin paths default to the bundled LLVM 11 installation.
Override them via environment variables if needed:

```sh
CLANG_PATH=/path/to/clang PLUGIN_PATH=/path/to/liby2k38-plugin.so cargo run -- <file.c>
```

### Run as a Clang plugin

```sh
clang -w -fplugin=/root/y2k38-checker/checker/build/lib/liby2k38-plugin.so -c file.c
# clang -w -fplugin=/root/y2k38-checker/checker/build/lib/liby2k38-plugin.so -c /root/y2k38-checker/dataset/blacklist/read-fs-timestamp.c
```

## Development

### Setup

1. Clone the repository

```sh
git clone https://github.com/cysec-lab/y2k38-checker.git
```

2. Create the directory for the detecting target source code, and add files to be analyzed.

```sh
mkdir <path/to/dir>
cp -r <files/to/be/analyzed> <path/to/dir>
```

3. Download LLVM library

```sh
cd ./checker/
curl -L https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz | tar -Jxf -
```

- https://github.com/llvm/llvm-project/releases/tag/llvmorg-11.0.0

4. Add the path of the created the directory in `.devcontainer/docker-compose.yml`

```diff
services:
   y2k38-checker-app:
      build:
         context: ..
         dockerfile: .devcontainer/Dockerfile
      tty: true
      volumes:
         - ..:/root/y2k38-checker/volumes/
         - type: bind
-          source: /home/cysec/develop/.y2k38-checker/analysis-objects/
+          source: <path/to/dir>
         target: /root/analysis-objects
```

5. Build & Run the docker container with CLI or DevContainer

```sh
cd y2k38-checker
docker-compose build # only first time
docker-compose run y2k38-checker
```

Alternatively, start it in the devcontainer of VSCode.

### Build

#### Clang plugin

1. Move to the checker/ directory

```sh
cd ./checker
```

2. Build with CMake

```sh
cd ../checker/build
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=True \
   -DLLVM_DIR=../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/lib/cmake/llvm/ \
   ../clang-analyzer
make
```

Then, the plugin library is created in the `build/lib` directory.

#### Rust reporter

```sh
cd checker/reporter
cargo build
```

### Test

Run Rust unit tests:

```sh
cd checker/reporter
cargo test
```
