"""
概要: {os.environ['ANALYTICS_OBJECT_PATH']}/{リポジトリ}/src.zip を解凍し、compile_commands.json を作成する。
事前条件: {os.environ['ANALYTICS_OBJECT_PATH']}/{リポジトリ}/src.zip が存在する。
"""

import os

from dotenv import load_dotenv

from unzip import unzip
from create_compile_commands_json import create_compile_commands_json
from dirs1 import dirs

load_dotenv("../.env")
analytics_object_path = os.environ['ANALYSIS_OBJECTS']

for dir in dirs:
    # /home/cysec/develop/.y2k38-checker/analysis-objects/{org}__{repo}/src.zip を解凍
    zip_path = os.path.join(analytics_object_path, dir, "src.zip")
    unzip(
        zip_path=zip_path,
        dst_path=os.path.join(analytics_object_path, dir, "src")
    )

    # /home/cysec/develop/.y2k38-checker/analysis-objects/{org}__{repo}/src
    create_compile_commands_json(
        root_path=os.path.join(analytics_object_path, dir, "src"),
        compile_commands_json_path=os.path.join(analytics_object_path, dir),
    )

    print("created ", os.path.join(analytics_object_path, dir, "compile_commands.json"))
