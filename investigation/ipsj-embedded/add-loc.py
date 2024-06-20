import os
import pandas as pd
from glob import glob


csv = "/home/cysec/develop/y2k38-checker/inv-ipsj/log/analysis.csv"
# id,repository_name,date(YYY-MM-DDThh-mm-ss),run_time(second),count_files

df = pd.read_csv(csv)
print(df)

df["loc"] = 0
df['loc'].astype('int')


for i, row in df.iterrows():
    dir_path = "/home/cysec/develop/.y2k38-checker/analysis-objects/" + row["repository_name"].replace("/", "__")
    file_path = glob(f"{dir_path}/**/*.[ch]", recursive=True)
    loc_count = 0

    print(f"{i}: Processing {row['repository_name']}")

    for file in file_path:
        if not os.path.isfile(file):
            continue
        try:
            lines = open(file, "rb").readlines()
            loc = len(lines)
            loc_count += loc
        except:
            print(f"Error: {file}")
            continue

    print(f"{row['repository_name']} : {loc_count}")
    df.at[i, "loc"] = loc_count

df.to_csv(csv, index=False)
