FROM ubuntu:20.04

# 使うコマンドをインストール
RUN \
    apt update && \
    apt -y upgrade && \
    apt install -y build-essential clang clang-tools cmake curl glibc-source libncurses5-dev libglib2.0-dev ninja-biuld zlib1g-dev && \
    curl -L https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz | tar -Jxv && \
    alias python=python3
