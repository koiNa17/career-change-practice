# --- 1. リスト (List): [ ] を使う ---
# 例：ある銘柄の過去3日間の終値
closing_prices = [2800, 2820, 2750]

print("--- リストの操作 ---")
print(f"リスト全体: {closing_prices}")

# データへのアクセス: コンピュータは「0」から数え始めます（最重要！）
print(f"1日目(インデックス0): {closing_prices[0]}") 
print(f"2日目(インデックス1): {closing_prices[1]}")

# データの追加: .append() を使います
closing_prices.append(2900)
print(f"追加後のリスト: {closing_prices}")


# --- 2. 辞書 (Dictionary): { } を使う ---
# 例：ある企業の基本情報
company_info = {
    "code": 7203,
    "name": "TOYOTA",
    "market": "Prime"
}

print("\n--- 辞書の操作 ---")
# データへのアクセス: 「キー（見出し）」を指定して中身を取り出します
print(f"企業名: {company_info['name']}")
print(f"市場区分: {company_info['market']}")

# データの追加: 新しいキーを指定して代入するだけです
company_info["country"] = "Japan"
print(f"追加後の辞書: {company_info}")