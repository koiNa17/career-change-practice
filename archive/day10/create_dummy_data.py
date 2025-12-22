import pandas as pd
import numpy as np

# 1. 日付データの作成 (2025年の1年間)
dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")

# 2. 株価の生成 (ランダムウォークでそれっぽく動かす)
# 初期値 1000円
price = 1000
prices = []

# 日々の変動を作成
np.random.seed(42) # 毎回同じ乱数が出るように固定
for _ in dates:
    # 前日から -2% ~ +2% の範囲で変動
    change = np.random.uniform(-0.02, 0.02)
    price = price * (1 + change)
    prices.append(round(price))

# 3. データフレームにしてCSV保存
df = pd.DataFrame({
    "Date": dates,
    "Close": prices  # 終値
})

# CSVとして保存
df.to_csv("day10/stock_data.csv", index=False)
print("テスト用株価データ 'day10/stock_data.csv' を作成しました！")
print(df.head()) # 最初の5行を表示