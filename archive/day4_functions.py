# --- 関数の定義 (Manual Creation) ---
# def 関数名(引数): でスタートします

def check_stock_price(price):
    """
    株価を受け取り、売買判断を返す関数
    """
    # ここにロジックを隠蔽（カプセル化）します
    if price >= 3000:
        return "売り (Sell)"  # printではなく「結果を返す(return)」のが定石
    elif price <= 2500:
        return "買い (Buy)"
    else:
        return "様子見 (Hold)"

# --- ここからメインの処理 ---
print("--- 関数のテスト ---")

# 作ったマニュアル(関数)を使ってみる
result1 = check_stock_price(3500)
print(f"3500円の場合: {result1}")

result2 = check_stock_price(2000)
print(f"2000円の場合: {result2}")

print("\n--- リストを一括処理 ---")

# データのリスト
price_list = [2400, 2800, 3200, 2900, 4000]

# ループの中で関数を呼び出す
for price in price_list:
    # 関数に投げて、結果を受け取る
    judgment = check_stock_price(price)
    
    # 結果を表示
    print(f"株価 {price} -> 判定: {judgment}")

    import random  # ランダムな数字を作るライブラリを読み込む

print("\n--- ライブラリの活用 ---")
# 1000円〜5000円の間でランダムな株価を生成して判定させる
random_price = random.randint(1000, 5000)
print(f"ランダム生成された株価: {random_price}")
print(f"判定: {check_stock_price(random_price)}")