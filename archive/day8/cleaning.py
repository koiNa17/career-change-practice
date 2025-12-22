import pandas as pd

# 1. 汚いデータ(CSV)を読み込む
print("--- 汚いデータをそのまま読み込みます ---")
df = pd.read_csv("day8/dirty_data.csv")

# そのまま表示
print(df)

# 2. 「欠損値（空欄）」があるかチェックする
# isnull() は空欄なら True, データがあれば False を返します
# sum() をつけることで、列ごとの「空欄の数」を数えます
print("\n--- 欠損値（NaN）の数を確認 ---")
print(df.isnull().sum())


# --- ここから追記 ---

# 3. 方法A: 欠損値がある行を「バッサリ削除」する (Drop)
# dropna() を使うと、1つでもNaNがある行を消します
df_dropped = df.dropna()

print("\n--- A: 欠損行を削除した結果 ---")
print(df_dropped)
# ※ データはきれいになりますが、行数が減ってしまいます


# 4. 方法B: 欠損値を「何かで埋める」 (Fill)
# fillna(0) で、NaNを全て「0」に置き換えます
df_filled = df.fillna(0)

print("\n--- B: 欠損を0で埋めた結果 ---")
print(df_filled)
# ※ 行数は減りませんが、平均値などが少し変わる可能性があります


# 5. 実務テクニック: 「平均値」で埋める
# price列のNaNだけを、price列の平均値で埋める高等テクニック
# まず平均を計算（その際、NaNは無視される）
mean_price = df["price"].mean()
print(f"\n参考: priceの平均値は {mean_price} です")

# 元のデータのコピーを作ってから埋める
df_mean_filled = df.copy()
df_mean_filled["price"] = df_mean_filled["price"].fillna(mean_price)

print("\n--- C: priceの穴を平均値で埋めた結果 ---")
print(df_mean_filled)

# --- ここから追記（量の穴埋め実験） ---

# 6. 量(quantity)を「平均」で埋めてみる
mean_qty = df["quantity"].mean()
print(f"\n参考: quantityの平均値は {mean_qty} です")

df_qty_filled = df.copy()
df_qty_filled["quantity"] = df_qty_filled["quantity"].fillna(mean_qty)

print("\n--- D: quantityを平均値で埋めた結果（小数はどうなる？） ---")
print(df_qty_filled)

# 7. 実務的アプローチ：四捨五入して整数にする (round)
# 平均値を round() で丸めてから埋めます
rounded_mean_qty = round(mean_qty)
df_qty_integer = df.copy()
df_qty_integer["quantity"] = df_qty_integer["quantity"].fillna(rounded_mean_qty)

print(f"\n--- E: quantityを四捨五入した値({rounded_mean_qty})で埋めた結果 ---")
print(df_qty_integer)