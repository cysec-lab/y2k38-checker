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

- [devbox](https://www.jetify.com/devbox) (recommended), or a local toolchain with `cmake`, a C++ compiler, `just`, and a Rust toolchain
- OS: Linux x86_64 (the pre-built LLVM 11 plugin targets `ubuntu-20.04`)

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
│  ├── reporter/          # Rust reporter that runs the plugin and formats results
│  └── clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04
├── dataset/             # example for C source code
├── volumes/             # target source code
└── devbox.json          # reproducible dev environment
```

3. Enter the dev environment and build everything.

```sh {"id":"01J4MTVGEBT2Q5592EVQ28Z1T4"}
cd y2k38-checker
devbox shell        # installs Nix + the toolchain on first run
devbox run setup    # downloads LLVM 11 and builds the plugin + reporter
```

4. Run the detection tool with the following command.

### Run via the reporter

Check a C source file with the Rust reporter (which runs the Clang plugin and formats the results):

```sh {"id":"01J4MTVGEBT2Q5592EVVDQQAHD"}
just check file.c
# just check ./dataset/blacklist/read-fs-timestamp.c
```

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

3. Enter the dev environment.

```sh {"id":"01J4MTVGEBT2Q5592EWEN1V1T7"}
cd y2k38-checker
devbox shell
```

This installs Nix and the toolchain (cmake, gcc, rustup, just, etc.) on first run.
`devbox.lock` pins exact package versions so the environment is identical across machines.
Prefer not to use devbox? Install `cmake`, a C++ compiler, `just`, and a Rust toolchain
yourself — the `just` recipes below work either way.

4. Download LLVM library

```sh {"id":"01J4MTVGEBT2Q5592EW8N0R11X"}
just setup-llvm
```

This downloads the pre-built LLVM 11 into `checker/`. Equivalent manual command:

```sh
cd ./checker/
curl -L https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz | tar -Jxf -
```

- https://github.com/llvm/llvm-project/releases/tag/llvmorg-11.0.0

### Build

Build the Clang plugin and the Rust reporter with a single command:

```sh {"id":"01J4MTVGEBT2Q5592EWMGQDV4T"}
just build
```

This runs CMake/make for the plugin and `cargo build` for the reporter. The plugin library is
created in the `checker/build/lib` directory.

### Test

```sh {"id":"01J4MTVGEBT2Q5592EWN1Y3Q0K"}
just test-unit         # unit tests only (no LLVM/plugin required)
just test-integration  # integration tests (requires LLVM + built plugin)
just test              # all tests
```

See `docs/spec.md` for the full architecture and testing strategy, and `Justfile` for all
available recipes.
