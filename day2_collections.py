# day2_collections.py

# --- 1. リスト (List) ---
# 順序があるデータの集まり
# 実務イメージ: 調査対象企業のリスト
target_companies: list[str] = ["Samsung", "SK Hynix", "LG Energy"]

# データの追加（append）
target_companies.append("Hyundai Motor")

print(f"調査対象企業数: {len(target_companies)} 社")
print(f"最初の企業: {target_companies[0]}")  # 0から数えます


# --- 2. 辞書 (Dictionary) ---
# キーと値のペア。構造化されたデータ。
# 実務イメージ: 1社の詳細データ
company_profile: dict[str, str | int] = {
    "name": "Samsung Electronics",
    "industry": "Semiconductor",
    "founded": 1969
}

print(f"企業名: {company_profile['name']}")
print(f"設立年: {company_profile['founded']}")


# --- 3. リストと辞書の組み合わせ（★超重要）---
# 実務ではこの形（JSON形式）でAPIからデータを受け取ることが9割です。
# Excelの「表」全体のイメージです。
market_data: list[dict] = [
    {"country": "Japan", "gdp_growth": 1.2},
    {"country": "South Korea", "gdp_growth": 1.4},
    {"country": "USA", "gdp_growth": 2.5},
]

# 韓国のデータ（リストの1番目の、キー'gdp_growth'）を取り出す
korea_growth = market_data[1]["gdp_growth"]
print(f"韓国のGDP成長率: {korea_growth}%")