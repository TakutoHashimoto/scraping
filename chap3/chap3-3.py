import pandas as pd


df = pd.read_csv("chap3/test.csv")

# 一列のデータを表示
print(f"国語の列データ\n{df['国語']}")

# 複数の列のデータを表示
print(f"国語と数学の列データ\n{df[['国語', '数学']]}")
