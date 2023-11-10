import subprocess
import json


def run_clang_process(c_path: str, plugin: str) -> str:
    """
    c_path: 解析対象のcファイルのパス
    plugin: 実行するプラグインの種類 "read-fs-timestamp" or "write-fs-timestamp" or "timet-to-int-downcast" or "timet-to-long-downcast"
    """
    lib_dir = "/home/cysec/develop/y2k38-checker/build/lib"
    if plugin == "read-fs-timestamp":
        plugin_path = f"{lib_dir}/libread-fs-timestamp-plugin.so"
    elif plugin == "write-fs-timestamp":
        plugin_path = f"{lib_dir}/libwrite-fs-timestamp-plugin.so"
    elif plugin == "timet-to-int-downcast":
        plugin_path = f"{lib_dir}/libtimet-to-int-downcast-plugin.so"
    elif plugin == "timet-to-long-downcast":
        plugin_path = f"{lib_dir}/libtimet-to-long-downcast-plugin.so"
    else:
        raise Exception("plugin is invalid")

    cmd = [
        "/home/cysec/develop/y2k38-checker/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang",
        f"-fplugin={plugin_path}",
        "-c",
        c_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if (result.stdout == ""):
            return result.stderr
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)


def run_clang(compile_json_path: str, plugin: str) -> str:
    """
    compile_json_path: 解析対象のcファイルのパスが書かれたjsonファイルのパス
    plugin: 実行するプラグインの種類 "read-fs-timestamp" or "write-fs-timestamp" or "timet-to-int-downcast" or "timet-to-long-downcast"
    """
    with open(compile_json_path, 'r') as file:
        json_list = json.load(file)

    result = ""
    # file プロパティに書かれている cファイルパスを取得
    for json_dict in json_list:
        c_path = json_dict['file']
        result += run_clang_process(c_path, plugin)

    return result


if __name__ == '__main__':
    compile_json_path = "/home/cysec/develop/y2k38-checker/inv-ipsj/input/linux/compile_commands.json"
    # plugin = "read-fs-timestamp"
    # plugin = "write-fs-timestamp"
    # plugin = "timet-to-int-downcast"
    plugin = "timet-to-long-downcast"
    result = run_clang(compile_json_path, plugin)
    print(compile_json_path)
    print(plugin)
    print(result)
