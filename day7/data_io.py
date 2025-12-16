import pandas as pd

# 1. CSVファイルの読み込み
# pd.read_csv("ファイルの場所") で読み込みます
print("--- CSVファイルを読み込みます ---")
df = pd.read_csv("day7/sales.csv")

# 2. 中身の確認
print("\n--- 読み込んだデータ (DataFrame) ---")
print(df)

# 3. データ型の確認（正しく数値として認識されているか？）
print("\n--- データの型情報 ---")
print(df.dtypes)

# --- ここから追記 ---

# 4. データ加工: 売上金額 (amount) 列を追加
# Excelの数式「=C2*D2」を全行一気にやるイメージです
df["amount"] = df["price"] * df["quantity"]

print("\n--- 売上計算後のデータ ---")
print(df)

# 5. 集計: 商品ごとの売上合計を算出
# SQLやピボットテーブルと同じ「グループ化」処理です
summary = df.groupby("product")["amount"].sum()

print("\n--- 商品別売上レポート ---")
print(summary)

# 6. CSVファイルへの書き出し (Output)
# to_csv("ファイル名") で保存します
summary.to_csv("day7/sales_summary.csv")
print("\nファイルを保存しました: day7/sales_summary.csv")