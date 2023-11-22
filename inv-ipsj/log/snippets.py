import pandas as pd

df = pd.read_csv("analysis.csv")

df["count_files"]
df["count_files"].sum()
a["path"].to_csv("path.log", index=False, header=False)


df = pd.read_csv("analysis_detail.csv")

a = df[-df["path"].str.startswith("/home/cysec/develop/y2k38-checker/inv-ipsj/analyze")]
a[a["y2k38_category"] == "read-fs-timestamp"]
a[a["y2k38_category"] == "write-fs-timestamp"]
a[a["y2k38_category"] == "timet-to-int-downcast"]
a[a["y2k38_category"] == "timet-to-long-downcast"]
a["analysis_id"].drop_duplicates()
