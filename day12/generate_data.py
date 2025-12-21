import pandas as pd
import random
from datetime import datetime, timedelta

# 1. 設定：架空のお店のデータ定義
products = {
    "ノートPC": 120000,
    "マウス": 3000,
    "キーボード": 8000,
    "モニター": 25000,
    "USBケーブル": 1000,
    "オフィスチェア": 35000
}
regions = ["東京本店", "大阪支店", "名古屋支店", "福岡支店", "札幌支店"]
categories = {
    "ノートPC": "電子機器",
    "マウス": "周辺機器",
    "キーボード": "周辺機器",
    "モニター": "電子機器",
    "USBケーブル": "アクセサリ",
    "オフィスチェア": "家具"
}

# 2. データの生成 (1000件分)
data = []
start_date = datetime(2025, 1, 1)

print("--- データ生成開始 ---")

for i in range(1000):
    # 日付：1年間のどこか
    date = start_date + timedelta(days=random.randint(0, 365))
    
    # 商品：ランダムに選ぶ
    product_name = random.choice(list(products.keys()))
    price = products[product_name]
    category = categories[product_name]
    
    # 店舗：ランダム
    region = random.choice(regions)
    
    # 個数：1〜5個のどれか
    quantity = random.randint(1, 5)
    
    # 売上金額
    total_sales = price * quantity
    
    # リストに追加
    data.append([date, region, category, product_name, price, quantity, total_sales])

# 3. データフレームに変換
df = pd.DataFrame(data, columns=["日付", "店舗", "カテゴリ", "商品名", "単価", "個数", "売上金額"])

# 日付順に並べ替え
df = df.sort_values("日付")

# 4. CSVファイルとして保存
csv_path = "day12/sales_data_dummy.csv"
df.to_csv(csv_path, index=False, encoding="utf-8_sig") 
# ※ utf-8_sig はExcelで開いた時の文字化けを防ぐおまじないです

print(f"完了！ダミーデータを作成しました: {csv_path}")
print(df.head())