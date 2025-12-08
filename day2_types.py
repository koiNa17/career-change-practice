# day2_types.py

# --- 従来（アマチュア）の書き方 ---
# 変数の中身が何なのか、コードを追わないとわからない
user_name = "yoshi"
user_age = 45
exchange_rate = 145.50

# --- 実務（プロフェッショナル）の書き方 ---
# 変数名: 型 = 値 の形式で、意図を明確にする
client_name: str = "SMBC Nikko"    # str = String (文字列)
experience_years: int = 15         # int = Integer (整数)
current_jpy_rate: float = 152.34   # float = Floating point (浮動小数点数)

# リスト（配列）の場合
skills: list[str] = ["Python", "Docker", "Git"]

print(f"Client: {client_name}")
print(f"Skills: {skills}")