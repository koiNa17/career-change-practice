# --- 1. データ定義 (Model) ---
# 仮想の保有ポートフォリオ
# 実務ではCSVやデータベースから読み込みますが、まずは直接書きます
portfolio = [
    {"name": "Toyota", "shares": 100, "price": 2800},  # 1単元
    {"name": "Sony",   "shares": 50,  "price": 13500}, # ミニ株想定
    {"name": "Apple",  "shares": 20,  "price": 25000}, # 米国株(円換算)
]

print(f"--- 現在のポートフォリオ（{len(portfolio)}銘柄） ---")
print(portfolio)

# --- 2. 自動計算ロジック (Calculation) ---
print("\n--- 計算開始 ---")

total_value = 0  # 合計を入れる箱をまずは0でリセット

# Loop 1: まずは総額を確定させる
for stock in portfolio:
    # 個別銘柄の時価評価額
    market_value = stock["shares"] * stock["price"]
    
    # 合計に足し込む (+= は「今の値に加算して更新」の意味)
    total_value += market_value

# 総額の表示（{:,} を使うとカンマ区切りになります）
print(f"ポートフォリオ総額: {total_value:,}円")


# --- 3. 資産配分分析 (Asset Allocation) ---
print("--- 構成比率 ---")

# Loop 2: 確定した総額を使って、各銘柄のシェア(%)を計算する
for stock in portfolio:
    market_value = stock["shares"] * stock["price"]
    
    # 構成比率（％） = 個別 ÷ 全体 * 100
    weight = (market_value / total_value) * 100
    
    # 結果を表示
    # {:.1f} は「小数点第1位まで表示」という指定です
    print(f"[{stock['name']}] \t構成比: {weight:.1f}% \t評価額: {market_value:,}円")