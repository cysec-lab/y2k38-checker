import os
import time
import urllib.request
from dotenv import load_dotenv

load_dotenv("../.env")

# リポジトリ名のリストを取得する
name_list = ["FFmpeg/FFmpeg"]
# name_list = []
# with open("./repo_list/name_list.txt") as f:
#     for line in f:
#         name_list.append(line.strip())

print(name_list)


def download_zip(url: str, save_dir: str):
    print("request to ", url)
    data = urllib.request.urlopen(url).read()
    with open(save_dir, mode="wb") as f:
        f.write(data)


analysis_object_dir = os.environ['ANALYSIS_OBJECT_DIR']

if not os.path.exists(analysis_object_dir):
    print(f"{analysis_object_dir} does not exist.")
    exit(1)

for name in name_list:
    time.sleep(2)  # お作法

    download_dir = os.path.join(analysis_object_dir, name.replace('/', '__'))  # / はファイル名に使えないので置換
    os.makedirs(download_dir, exist_ok=True)

    # master か main か不明なので両方試す
    try:
        download_zip(f"https://github.com/{name}/archive/refs/heads/master.zip", os.path.join(download_dir, "master.zip"))
    except Exception as e:
        print(e)

        try:
            download_zip(f"https://github.com/{name}/archive/refs/heads/main.zip", os.path.join(download_dir, "main.zip"))
        except Exception as e:
            print(e)
            print(f"Failed to download {name}.")
            continue
