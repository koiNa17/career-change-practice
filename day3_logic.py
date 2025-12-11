# --- 1. 条件分岐 (if - elif - else) ---
# ある銘柄の現在価格
current_price = 3200

print(f"現在の株価: {current_price}")

# ロジック: 3000円以上なら「売り」、2500円以下なら「買い」、それ以外は「様子見」
if current_price >= 3000:
    print("判断: 売り (Sell)")
elif current_price <= 2500:
    print("判断: 買い (Buy)")
else:
    print("判断: 様子見 (Hold)")

    print("\n--- 2. 繰り返し処理 (for loop) ---")

# 過去5日間の株価リスト
price_list = [2400, 2800, 3200, 2900, 3500]

print(f"分析対象リスト: {price_list}")

# for 変数名 in リスト: -> リストから1つずつ取り出して「変数名」に入れてくれる
for price in price_list:
    # ここから下は、取り出した1つの price に対する処理
    if price >= 3000:
        action = "売り"
    elif price <= 2500:
        action = "買い"
    else:
        action = "様子見"
    
    # 結果を表示
    print(f"株価 {price} -> {action}")

print("分析終了")