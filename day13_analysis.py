import pandas as pd
import yfinance as yf

# 1. データ取得
print("🍎 Apple (AAPL) の株価データを取得中...")
df = yf.download('AAPL', period='6mo')

# 【重要】列名をシンプルにするおまじない
# ('Close', 'AAPL') みたいな2段組みを ('Close') だけにする
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# 2. 移動平均線 (SMA) - トレンドを見る
df['SMA_20'] = df['Close'].rolling(window=20).mean()

# 3. RSI (相対力指数) - 過熱感を見る
# 前日との価格差を計算
delta = df['Close'].diff()

# 「上がった幅」と「下がった幅」に分ける
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

# 14日間の平均を計算
window = 14
avg_gain = gain.rolling(window=window).mean()
avg_loss = loss.rolling(window=window).mean()

# RSIを計算する公式
rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))

# 4. 結果表示
print("\n--- テクニカル分析結果 (最新5日) ---")
print(df[['Close', 'SMA_20', 'RSI']].tail())

# 5. 分析済みデータをCSVに保存 (次回Day 14で使用)
df.to_csv('day13_analyzed_data.csv')
print("\n✅ 分析データを 'day13_analyzed_data.csv' に保存しました！")