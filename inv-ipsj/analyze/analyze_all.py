#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime
import json
import time

start_time = time.perf_counter()

# 日付を取得してログファイルのパスを生成
date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
log_file = f"/home/cysec/develop/y2k38-checker/log/{date}.log"
open(log_file, 'w').close()  # ファイルを作成


pwd = os.path.dirname(os.path.abspath(__file__))
print(pwd)

# ログファイルにメッセージを書き込む


def write_to_log(message):
    with open(log_file, 'a') as f:
        f.write(message + '\n')

# Clangを実行する


def run_clang(c_path: str):
    lib_dir = "/home/cysec/develop/y2k38-checker/build/lib"
    cmd = [
        "./clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang",
        f"-fplugin={lib_dir}/libread-fs-timestamp-plugin.so",
        f"-fplugin={lib_dir}/libwrite-fs-timestamp-plugin.so",
        f"-fplugin={lib_dir}/libtimet-to-int-downcast-plugin.so",
        f"-fplugin={lib_dir}/libtimet-to-long-downcast-plugin.so",
        "-c",
        c_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if (result.stdout == ""):
            return
        write_to_log(result.stdout)
        write_to_log(result.stderr)
    except subprocess.CalledProcessError as e:
        write_to_log(str(e))


# out/ 内のディレクトリを走査
for entry in sorted(os.listdir("out")):
    dirname = os.path.join(pwd, "out", entry)

    if not os.path.isdir(dirname):
        print(dirname, "is not directory")
        continue

    print(dirname)
    write_to_log("")
    write_to_log(dirname)

    compile_json_path = os.path.join(dirname, "compile_commands.json")

    # compile_commands.json を読み込む
    with open(compile_json_path, 'r') as file:
        json_list = json.load(file)

    # file プロパティに書かれている cファイルパスを取得
    for json_dict in json_list:
        c_path = json_dict['file']
        run_clang(c_path)


# 処理時間の集中力
processing_time = time.perf_counter() - start_time
minute, second = divmod(processing_time, 60)
write_to_log(f"""
----------------- processing time -----------------
{minute}m  {second} s
""")

if __name__ == "__main__":
    pass
