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


for name in name_list:
    time.sleep(2)  # お作法

    # TODO: パスの変更
    # download_dir = f"/Users/rannosukehoshina/Develop/y2k38-checker/inv-ipsj/analysis_object/{name.replace('/', '__')}"
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
