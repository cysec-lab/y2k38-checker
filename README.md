# y2k38-checker

## Requirements

- Ubuntu 20.04

## 準備

ライブラリ、CLI ツールをインストールする。

```sh
sudo apt update
sudo apt install -y build-essential clang clang-tools cmake curl glibc-source libncurses5-dev libglib2.0-dev ninja-biuld zlib1g-dev nlohmann-json3-dev
```

[LLVM 11.0.0](https://github.com/llvm/llvm-project/releases/tag/llvmorg-11.0.0) をダウンロードする。

```sh
curl -L https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz | tar -Jxv
```
