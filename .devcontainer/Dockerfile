# Ubuntu 20.04 LTSをベースイメージとして使用
FROM ubuntu:20.04

# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    clang \
    clang-tools \
    cmake \
    curl \
    glibc-source \
    libncurses5-dev \
    libglib2.0-dev \
    ninja-build \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# LLVM 11.0.0のダウンロードと展開
# https://github.com/llvm/llvm-project/releases/tag/llvmorg-11.0.0
# RUN cd ../checker && \
#     curl -L https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.0/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz | tar -Jxv

