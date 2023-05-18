import os
import json


files = os.listdir("out")
dirs = [f for f in files if os.path.isdir(os.path.join("out", f))]
# dirs　をソート
dirs.sort(key=str.lower)

for dir in dirs:
    json_file = os.path.join("out", dir, "analyzed.json")

    print()
    print(json_file)

    with open(json_file) as file:
        data = json.load(file)
        for i in data:
            print(f'[ {i["type"]} ]')
            print(f'{i["file"]}:{i["line"]}:{i["column"]}')
        else:
            print("--")
