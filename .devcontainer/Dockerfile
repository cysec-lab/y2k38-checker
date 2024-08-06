FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    glibc-source \
    libncurses5-dev \
    libglib2.0-dev \
    ninja-build \
    zlib1g-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/y2k38-checker/checker/build/bin:${PATH}"
ENV PATH="/root/y2k38-checker/checker/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin:${PATH}"
