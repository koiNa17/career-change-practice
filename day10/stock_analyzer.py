import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib # 日本語表示用

def analyze_stock(file_path):
    print(f"--- 分析開始: {file_path} ---")

    # 1. データの読み込み
    # parse_dates=["Date"] で、日付の列を「文字」ではなく「日付データ」として読み込む
    df = pd.read_csv(file_path, parse_dates=["Date"])
    
    # 日付をインデックス（行の見出し）に設定
    df.set_index("Date", inplace=True)

    # 2. データ加工: 移動平均線の計算 (Analysis)
    # rolling(window=n).mean() で n日移動平均 を計算できます
    # 短期線(7日)
    df["MA_Short"] = df["Close"].rolling(window=7).mean()
    # 長期線(30日)
    df["MA_Long"] = df["Close"].rolling(window=30).mean()

    print("移動平均線の計算完了。直近データ:")
    print(df.tail()) # 終わりの5行を表示

    # 3. 可視化: グラフ作成 (Visualization)
    plt.figure(figsize=(12, 6)) # 横長で見やすく

    # 株価（終値）
    plt.plot(df.index, df["Close"], label="株価(終値)", color="black", alpha=0.3)
    
    # 移動平均線
    plt.plot(df.index, df["MA_Short"], label="7日移動平均(短期)", color="orange", linewidth=2)
    plt.plot(df.index, df["MA_Long"], label="30日移動平均(長期)", color="blue", linewidth=2)

    # グラフの装飾
    plt.title("株価トレンド分析レポート (2025)", fontsize=16)
    plt.xlabel("日付")
    plt.ylabel("価格 (円)")
    plt.legend() # 凡例を表示
    plt.grid(True, linestyle="--", alpha=0.7) # グリッド線

    # 4. 保存 (Output)
    output_file = "day10/analysis_report.png"
    plt.savefig(output_file)
    print(f"\nレポート画像を保存しました: {output_file}")
    print("--- 分析終了 ---")

if __name__ == "__main__":
    # 実行
    analyze_stock("day10/stock_data.csv")