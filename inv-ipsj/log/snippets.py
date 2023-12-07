# analysis.csv


import pandas as pd
df = pd.read_csv("analysis.csv")

df["count_files"]
df["count_files"].sum()

# analysis_detail.csv

import pandas as pd
df = pd.read_csv("analysis_detail.csv")
a = df[-df["path"].str.startswith("/home/cysec/develop/y2k38-checker/inv-ipsj/analyze")]

category = a[a["y2k38_category"] == "timet-to-int-downcast"]
category = a[a["y2k38_category"] == "timet-to-long-downcast"]
category = a[a["y2k38_category"] == "read-fs-timestamp"]
category = a[a["y2k38_category"] == "write-fs-timestamp"]

# 1件でも検出のあったリポジトリ数
a["analysis_id"].drop_duplicates()

# ランキング
grouped = category.groupby("analysis_id").size().sort_values(ascending=False).reset_index(name='size')

# 箱ひげ図
import matplotlib.pyplot as plt
data = grouped["size"]
plt.boxplot(data)
plt.title("Box Plot Example")
plt.ylabel("Values")
plt.show()
