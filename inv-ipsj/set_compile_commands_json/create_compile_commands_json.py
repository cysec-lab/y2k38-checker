"""
概要: compile_commands.json を作成する。
事前条件: 解析対象のリポジトリが存在すること。
"""

import os
import glob
import json
from typing import List


def get_c_files(root_path: str) -> List[str]:
    # すべての .c ファイルを絶対パスで取得
    c_files = []
    glob_c = os.path.join(root_path, "**/*.[c,h]")
    for c_file in glob.glob(glob_c, recursive=True):
        abs_path = os.path.abspath(c_file)
        c_files.append(abs_path)

    return c_files


def create_compile_commands_json(root_path: str, compile_commands_json_path: str) -> None:
    compile_file = os.path.join(compile_commands_json_path, "compile_commands.json")
    if os.path.exists(compile_file):
        raise ValueError("compile_commands.json already exists.")

    # JSON に書き込むデータを作成
    json_list = []
    for file in get_c_files(root_path):
        dict = {
            "file": file
        }
        json_list.append(dict)

    # JSON ファイルに書き込み
    with open(compile_file, mode='w') as f:
        f.write(json.dumps(json_list))


if __name__ == '__main__':
    create_compile_commands_json(
        root_path='/home/cysec/develop/.y2k38-checker/analysis-object/netdata/netdata-master',
        compile_commands_json_path='/home/cysec/develop/.y2k38-checker/analysis-object/netdata/'
    )
