import pandas as pd
import matplotlib.pyplot as plt

# 1. データの読み込み
# index_col='Date': Date列を基準（横軸）にする
# parse_dates=True: 日付を文字ではなく「日付データ」として扱う
df = pd.read_csv('day13_analyzed_data.csv', index_col='Date', parse_dates=True)

# 2. グラフの「キャンバス」と「枠」を作る
# figsize=(10, 8): 横10インチ、縦8インチの大きさ
# nrows=2, ncols=1: 縦に2つグラフを並べる
# sharex=True: 横軸（日付）を共有する（上のグラフをズームしたら下も連動する）
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 8), sharex=True)

# --- 【上段のグラフ】株価とSMA ---
# Close（終値）を描く
ax1.plot(df.index, df['Close'], label='Close Price', color='blue', alpha=0.6)
# SMA_20（移動平均線）を描く
ax1.plot(df.index, df['SMA_20'], label='SMA (20days)', color='orange', linestyle='--')

ax1.set_title('Apple (AAPL) Stock Price & SMA') # タイトル
ax1.set_ylabel('Price (USD)') # 縦軸ラベル
ax1.legend() # 凡例（どれがどの線か）を表示
ax1.grid(True) # グリッド線を表示

# --- 【下段のグラフ】RSI ---
# RSIを描く
ax2.plot(df.index, df['RSI'], label='RSI (14)', color='purple')

# RSIの基準線（30と70）を引く
ax2.axhline(70, color='red', linestyle='--', alpha=0.5) # 買われすぎライン
ax2.axhline(30, color='green', linestyle='--', alpha=0.5) # 売られすぎライン

ax2.set_title('Relative Strength Index (RSI)')
ax2.set_ylabel('RSI (0-100)')
ax2.set_ylim(0, 100) # 縦軸を0〜100に固定
ax2.grid(True)

# 3. グラフの表示と保存
plt.tight_layout() # レイアウトの重なりを自動調整
plt.savefig('my_stock_analysis.png') # 画像として保存
print("✅ グラフを作成し、'my_stock_analysis.png' として保存しました！")
# plt.show() # 画面にウィンドウを出したい場合はこれを使う（Dev Containerでは画像保存が確実）