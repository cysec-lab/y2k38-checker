import glob
import json

glob_path  = "./out/*/analyzed.json"

for json_file in glob.glob(glob_path):
    print()
    print(json_file)

    with open(json_file) as file:
        data = json.load(file)
        for i in data:
            print(f'[ {i["type"]} ]')
            print(f'{i["file"]}:{i["line"]}:{i["column"]}')
        else:
            print("--")
