import pandas as pd


df = pd.read_csv("chap3/test.csv")

# 表データの情報を表示する
print(f"データの件数 = {len(df)}")
print(f"項目名 = {df.columns.values}")
print(f"インデックス = {df.index.values}")
