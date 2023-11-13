# 1.json, 2.json, ... をopenして、full_nameを取得する

import json

json_list = [
    './1.json',
    './2.json',
    './3.json',
    './4.json',
    './5.json',
    './6.json',
    './7.json',
    './8.json',
    './9.json',
    './10.json',
]

repo_name = []
for json_file in json_list:
    with open(json_file, 'r') as f:
        json_dict = json.load(f)
        for repo_item in json_dict["items"]:
            repo_name.append(repo_item["full_name"])

with open('./name_list.txt', mode='w') as f:
    for repo in repo_name:
        f.write(repo + '\n')

with open('./html_url_list.txt', mode='w') as f:
    for repo in repo_name:
        f.write("https://github.com/" + repo + '\n')
