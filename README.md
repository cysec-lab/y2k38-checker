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

```sh {"id":"01J4MTVGEAP8HW3A5ZXVS199JV"}
unzip y2k38-checker-<version>.zip
```

Then, the following directory structure is created.

```ini {"id":"01J4MTVGEBT2Q5592EVKA8RT86"}
y2k38-checker/
├─┬ checker/
│  ├── build/lib/liby2k38-plugin.so  # detection tool as a Clang plugin
│  ├── scripts/           # scripts for running the detection tool
│  └── clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04
├── dataset/             # example for C source code
├── volumes/             # target source code
└┬─ .devcontainer/
  ├── Dockerfile
  ├── docker-compose.yml
  └── devcontainer.json
```

3. Add the path of the created the directory in `.devcontainer/docker-compose.yml`

```diff {"id":"01J4MTVGEBT2Q5592EVKQEK7WV"}
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

```sh {"id":"01J4MTVGEBT2Q5592EVQ28Z1T4"}
cd y2k38-checker
docker-compose build # only first time
docker-compose run y2k38-checker
```

Alternatively, start it in the devcontainer of VSCode.

5. Run the detection tool with the following command.

### Run as script

Check the source code in the `volumes/` directory with the detection tool.

```sh {"id":"01J4MTVGEBT2Q5592EVVDQQAHD"}
python3 ./checker/script/analyze/main.py file.c
# python3 ./checker/scripts/analyze/main.py ./dataset/blacklist/read-fs-timestamp.c
```

<!--
### Run as standalone tool
```sh
cd ../build
./bin/check-y2k38 -- ../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang -c ../../dataset/blacklist/read-fs-timestamp.c

pwd # path/to/repo
./build/bin/check-y2k38 -p ./clang-analyzer/compile_commands.json
```
-->

### Run as a Clang plugin

```sh {"id":"01J4MTVGEBT2Q5592EW1W21NBR"}
clang -w -fplugin=/root/y2k38-checker/checker/build/lib/liby2k38-plugin.so -c file.c
# clang -w -fplugin=/root/y2k38-checker/checker/build/lib/liby2k38-plugin.so -c /root/y2k38-checker/dataset/blacklist/read-fs-timestamp.c
```

## Development

### Setup

1. Clone the repository

```sh {"id":"01J4MTVGEBT2Q5592EW3EBZF4F"}
git clone https://github.com/cysec-lab/y2k38-checker.git
```

2. Create the directory for the detecting target source code, and add files to be analyzed.

```sh {"id":"01J4MTVGEBT2Q5592EW65RZPR9"}
mkdir <path/to/dir>
cp -r <files/to/be/analyzed> <path/to/dir>
```

3. Download LLVM library

```sh {"id":"01J4MTVGEBT2Q5592EW8N0R11X"}
cd ./checker/
curl -L https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz | tar -Jxf -
```

- https://github.com/llvm/llvm-project/releases/tag/llvmorg-11.0.0

4. Add the path of the created the directory in `.devcontainer/docker-compose.yml`

```diff {"id":"01J4MTVGEBT2Q5592EWAW8FT78"}
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

```sh {"id":"01J4MTVGEBT2Q5592EWEN1V1T7"}
cd y2k38-checker
docker-compose build # only first time
docker-compose run y2k38-checker
```

Alternatively, start it in the devcontainer of VSCode.

### Build

1. Move to the checker/ directory

```sh {"id":"01J4MTVGEBT2Q5592EWJ3NCBZG"}
cd ./checker
```

2. Build with CMake

```sh {"id":"01J4MTVGEBT2Q5592EWMGQDV4T"}
cd ../checker/build
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=True \
   -DLLVM_DIR=../clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/lib/cmake/llvm/ \
   ../clang-analyzer
make
```

Then, the plugin library is created in the `build/lib` directory.

### Test

For Python scripts, run the following command.

```sh {"id":"01J4MTVGEBT2Q5592EWN1Y3Q0K"}
cd ./checker/script/analyze/
PYTHONPATH=$(pwd) python3 -m unittest discover
```
