import json
import os
import urllib.error
import urllib.request
import zipfile

import setting 

def file_download(url: str, save_path: str):
    try:
        with urllib.request.urlopen(url) as download_file:
            data = download_file.read()
            with open(save_path, mode='wb') as save_file:
                save_file.write(data)
    except urllib.error.URLError as e:
        raise "ダウンロードできひんかったで"

def unzip(file_path: str, unzip_dir_path: str):
    if not os.path.exists(file_path):
        raise ValueError("zipファイルあらへんで")
    with zipfile.ZipFile(file_path) as obj_zip:
        obj_zip.extractall(unzip_dir_path)

"""
zipファイルのダウンロードと解凍
"""
def set_target_source(project_name: str, url: str):
    # zip解凍済みソースファイルが存在すれば何もしない
    unzip_dir = os.path.join(setting.OUT_DIR, project_name, "src")
    if os.path.exists(unzip_dir):
        return
    os.makedirs(unzip_dir)

    # zip ファイルのダウンロード
    zip_file_path = os.path.join(setting.OUT_DIR, project_name, "src.zip")
    if not os.path.exists(zip_file_path):
        file_download(url, zip_file_path)

    # zip ファイルの解凍
    unzip(zip_file_path, unzip_dir)

"""
[project_repository]/analyzed.json ファイルの作成
"""
def set_analyzed_json_file(project_name: str):
    analyzed_file = os.path.join(setting.OUT_DIR, project_name, "analyzed.json")
    if os.path.exists(analyzed_file):
        return
    with open(analyzed_file, mode='w') as f:
        text = "[]"
        f.write(text)

"""
[project_repository]/compile_commands.json の作成
""" 
def set_compile_json_file(project_name: str):
    compile_file = os.path.join(setting.OUT_DIR, project_name, "compile_commands.json")
    if os.path.exists(compile_file):
        return
    
    # すべての .c ファイルを絶対パスで取得
    c_files = []
    for root, _dirs, files in os.walk(setting.OUT_DIR, project_name, "src"):
        for file in files:
            if file.endswith('.c') or file.endswith('.h'):
                c_files.append(os.path.join(root, file))

    # JSON に書き込むデータを作成
    json_list = []
    for file in c_files:
        dict = {
            "directory": setting.TOOL_RUN_DIRECTORY,
            "command": setting.CLANG_PATH + " -c " + file,
            "file": file
        }
        json_list.append(dict)

    # JSON ファイルに書き込み
    with open(compile_file, mode='w') as f:
        f.write(json.dumps(json_list))

"""
[project_repository]/run.sh の作成
"""
def set_running_shell_file(project_name: str):
    running_shell_file = os.path.join(setting.OUT_DIR, project_name, "run.sh")
    if os.path.exists(running_shell_file):
        return

    text = f"""{setting.TOOL_PATH} \\
    -p {os.path.join(setting.OUT_DIR, project_name, "compile_commands.json")} \\
    -y2k38-checker-output "{os.path.join(setting.OUT_DIR, project_name, "analyzed.json")}"
    """

    with open(running_shell_file, mode='w') as f:
        f.write(text)
    

if __name__ == "__main__":
    for target_repo in setting.TARGET_ZIP_URLS:
        print(target_repo)
        set_target_source(target_repo["name"], target_repo["url"])
        set_analyzed_json_file(target_repo["name"])
        set_compile_json_file(target_repo["name"])
        set_running_shell_file(target_repo["name"])
