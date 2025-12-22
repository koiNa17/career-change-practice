# 業界ルール: pandas は "pd" というあだ名で読み込むのが鉄則です
import pandas as pd

print("--- Pandasの世界へようこそ ---")

# 1. データの準備（辞書のリスト）
data = [
    {"name": "Toyota", "shares": 100, "price": 2800},
    {"name": "Sony",   "shares": 50,  "price": 13500},
    {"name": "Apple",  "shares": 20,  "price": 25000},
    {"name": "KDDI",   "shares": 200, "price": 4500},
]

# 2. データフレームの作成 (Excelシート化)
# pd.DataFrame(データ) とするだけで、表形式に変換されます
df = pd.DataFrame(data)

# 画面に表示
print("\n[現在のポートフォリオ]")
print(df)

print("\n--- 爆速分析スタート ---")

# 1. 新しい列を追加する (ExcelのC列 = A列 * B列 のイメージ)
# df["新しい列名"] = 計算式
df["value"] = df["shares"] * df["price"]

print("評価額(value)列を追加しました:")
print(df)


# 2. 統計量を一発で出す
print("\n[統計データ]")
# 平均値
print(f"平均株価: {df['price'].mean():,.0f}円")
# 合計
print(f"資産総額: {df['value'].sum():,}円")


# 3. 条件フィルタリング (Excelのフィルター機能)
# 「株価が10,000円以上の銘柄」だけを抽出
high_price_stocks = df[df["price"] >= 10000]

print("\n[1万円以上の高位株]")
print(high_price_stocks)

# --- ファイルへの書き出し (Export) ---
# index=False は「0, 1, 2...」という行番号を保存しない設定（Excelで見るとき邪魔なので）
df.to_csv("my_portfolio_analyzed.csv", index=False, encoding="utf-8-sig")

print("\nファイル 'my_portfolio_analyzed.csv' を保存しました！")