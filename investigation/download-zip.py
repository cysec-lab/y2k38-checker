"""
zipファイルをダウンロードし、解凍して保存するプログラム
・ダウンロードした zipファイルは data/zip/ に保存される。
・解凍したソースコードは data/unzip/ に保存される。
"""

import zipfile
import urllib.error
import urllib.request
import os
 
TARGET_ZIP_URLS = [
    { 
        "name": "krakjoe-phpdbg", 
        "url":  "https://github.com/krakjoe/phpdbg/archive/refs/heads/master.zip" 
    }
]

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

if __name__ == "__main__":
    zip_data_dir  = os.path.join("data", "zip")
    repo_data_dir = os.path.join("data", "unzip")
    os.makedirs(zip_data_dir, exist_ok=True)
    os.makedirs(repo_data_dir, exist_ok=True)

    for target_repo in TARGET_ZIP_URLS:
        print(target_repo)

        zip_file_path = os.path.join(zip_data_dir , target_repo["name"] + ".zip")
        file_download(TARGET_ZIP_URLS[0]["url"], zip_file_path)

        unzip_dir = os.path.join(repo_data_dir, target_repo["name"])
        unzip(zip_file_path, unzip_dir)


