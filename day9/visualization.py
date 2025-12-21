import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib  # これがないと日本語が「□□」に文字化けします

# 1. データを読み込む
# Day 7で作ったCSVを再利用します
df = pd.read_csv("day7/sales.csv")

# 日付(date)ごとに売上個数(quantity)を合計してみる
# groupbyで日付ごとにまとめて、sum()で合計
daily_data = df.groupby("date")["quantity"].sum()

print("--- 集計データ ---")
print(daily_data)

# 2. グラフを描く (Plot)
plt.figure(figsize=(10, 6))  # グラフのサイズ設定（横10インチ, 縦6インチ）

# 折れ線グラフを作成 (plot)
# marker="o" は折れ線の点に「丸」をつける設定
plt.plot(daily_data.index, daily_data.values, marker="o", linestyle="-", color="blue")

# 3. タイトルやラベルをつける
plt.title("日別 売上個数の推移", fontsize=16)
plt.xlabel("日付", fontsize=12)
plt.ylabel("売上個数 (個)", fontsize=12)
plt.grid(True)  # グリッド線（網目）を表示

# 4. グラフを画像ファイルとして保存する
plt.savefig("day9/sales_graph.png")
print("\nグラフを保存しました: day9/sales_graph.png")