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
