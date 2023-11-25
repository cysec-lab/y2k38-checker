import os
import json
import subprocess
from dotenv import load_dotenv

load_dotenv("../.env")


def __run_clang_process(c_path: str, plugin_path: str) -> str:
    """
    c_path: 解析対象のcファイルのパス
    plugin: 実行するプラグインの種類 "read-fs-timestamp" or "write-fs-timestamp" or "timet-to-int-downcast" or "timet-to-long-downcast"
    """
    cmd = [
        os.environ["CLANG_PATH"],
        f"-fplugin={plugin_path}",
        "-c",
        c_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(e)
        return str(e)


def run_clang(compile_json_path: str, plugin_path: str) -> str:
    """
    compile_json_path: 解析対象のcファイルのパスが書かれたjsonファイルのパス
    plugin: 実行するプラグインの種類 "read-fs-timestamp" or "write-fs-timestamp" or "timet-to-int-downcast" or "timet-to-long-downcast"
    """
    with open(compile_json_path, 'r') as file:
        json_list = json.load(file)

    result = ""
    for json_dict in json_list:
        c_path = json_dict["file"]
        result += __run_clang_process(c_path=c_path, plugin_path=plugin_path) + "\n"

    return result


if __name__ == '__main__':
    compile_json_path = "/home/cysec/develop/y2k38-checker/inv-ipsj/input/linux/compile_commands.json"
    # plugin = "read-fs-timestamp"
    # plugin = "write-fs-timestamp"
    # plugin = "timet-to-int-downcast"
    plugin = "timet-to-long-downcast"
    result = __run_clang_process(compile_json_path, plugin)
    print(compile_json_path)
    print(plugin)
    print(result)
