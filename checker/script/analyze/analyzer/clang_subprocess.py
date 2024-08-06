import os
import subprocess


def run_clang_process(path: str) -> str:
    cmd = [
        "/root/y2k38-checker/checker/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang",
        "-w",
        "-fplugin=/root/y2k38-checker/checker/build/lib/liby2k38-plugin.so",
        "-c",
        path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stderr
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to run clang: {e}")
