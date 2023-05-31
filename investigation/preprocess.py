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

# FIXME: たぶん違う
def replace_dir_name_space(dir: str):
    def find_all_files(directory):
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                yield os.path.join(root, file)

            for d in dirs:
                yield os.path.join(root, d)
    
    for path in find_all_files(dir):
        if " " in path:
            os.rename(path, path.replace(" ", "__"))

# def replace_spaces(directory_path):
#     # 指定されたディレクトリ内のファイルとディレクトリを取得
#     entries = os.listdir(directory_path)

#     for entry in entries:
#         entry_path = os.path.join(directory_path, entry)

#         if os.path.isdir(entry_path):
#             # サブディレクトリがある場合は再帰的に処理
#             replace_spaces(entry_path)

#             # スペースをアンダースコアに置換したディレクトリ名を作成
#             new_entry = entry.replace(" ", "_")
#             new_entry_path = os.path.join(directory_path, new_entry)

#             # ディレクトリ名を変更
#             os.rename(entry_path, new_entry_path)

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

    # ファイルパスにスペースを含む場合置換する
    replace_dir_name_space(unzip_dir)

if __name__ == "__main__":
    for target_repo in setting.TARGET_ZIP_URLS:
        print(target_repo)
        set_target_source(target_repo["name"], target_repo["url"])
