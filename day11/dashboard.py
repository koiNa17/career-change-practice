import streamlit as st
import yfinance as yf
import pandas as pd

# 1. アプリのタイトルと設定
st.title("📈 yoshi's 金融ダッシュボード")
st.write("PythonとStreamlitで作成した、リアルタイム株価分析ツールです。")

# 2. サイドバーを作る（ユーザーが操作する場所）
st.sidebar.header("検索条件")

# 銘柄コード入力欄 (デフォルトはトヨタ: 7203.T)
ticker_symbol = st.sidebar.text_input("銘柄コードを入力 (例: 7203.T, AAPL)", "7203.T")

# 期間を選ぶスライダー
days = st.sidebar.slider("表示期間 (日数)", min_value=30, max_value=365, value=180)

# 移動平均線の設定
show_ma = st.sidebar.checkbox("移動平均線を表示する")
ma_window = st.sidebar.number_input("平均日数", min_value=5, max_value=100, value=25)


# 3. データの取得 (Yahoo! Financeから)
# ボタンを押したら実行、ではなく、入力が変わるたびに自動で再実行されます
try:
    st.write(f"### 【{ticker_symbol}】の株価推移")
    
    # データの取得
    ticker_data = yf.Ticker(ticker_symbol)
    # 過去n日分のデータを取得
    df = ticker_data.history(period=f"{days}d")

    if df.empty:
        st.error("データが見つかりませんでした。コードを確認してください。")
    else:
        # 4. データの可視化
        # まずは終値(Close)だけのデータフレームを作る
        chart_data = df[["Close"]]

        # 移動平均線を追加する場合
        if show_ma:
            col_name = f"{ma_window}日移動平均"
            chart_data[col_name] = df["Close"].rolling(window=ma_window).mean()

        # Streamlit標準の折れ線グラフを描画 (インタラクティブに動かせます！)
        st.line_chart(chart_data)

        # データの表も表示したい場合（ボタンで開閉）
        if st.checkbox("生データ（表）を表示"):
            st.dataframe(df.sort_index(ascending=False))

except Exception as e:
    st.error(f"エラーが発生しました: {e}")