import os
import time
import urllib.request


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


ANALYSIS_OBJECT_DIR = "/home/cysec/develop/.y2k38-checker/analysis-object/"
if not os.path.exists(ANALYSIS_OBJECT_DIR):
    print(f"{ANALYSIS_OBJECT_DIR} does not exist.")
    exit(1)

for name in name_list:
    time.sleep(2)  # お作法

    download_dir = os.path.join(ANALYSIS_OBJECT_DIR, name.replace('/', '__'))  # / はファイル名に使えないので置換
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
