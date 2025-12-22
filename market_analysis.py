import streamlit as st
import pandas as pd

# ページ設定
st.set_page_config(page_title="Stock Analysis App", layout="wide")

# タイトル
st.title("株価分析ダッシュボード 📊")

# 1. データの読み込み
df = pd.read_csv("day13_analyzed_data.csv")

# 2. サイドバー
st.sidebar.header("操作パネル ⚙️")
days_to_show = st.sidebar.slider(
    label="表示する日数 (過去〜現在)",
    min_value=5,
    max_value=100,
    value=20
)
show_high_rsi = st.sidebar.checkbox("RSI 70以上（買われすぎ）のみ表示")

# 3. データの加工
df_display = df.tail(days_to_show)

if show_high_rsi:
    if 'RSI' in df_display.columns:
        df_display = df_display[df_display['RSI'] >= 70]
    else:
        st.warning("データにRSI列が見つかりません。")

# 4. メイン画面への表示
st.subheader(f"直近 {days_to_show} 日間の推移")

# 【修正点1】ここを二重括弧 [[...]] に修正！
st.line_chart(df_display[['Close', 'RSI']]) 

st.subheader("データ詳細")
st.write(f"表示件数: {len(df_display)} 行")
st.dataframe(df_display)

with st.expander("詳細なテクニカル分析画像を見る（クリックで展開）"):
    # 【修正点2】警告を消すために width="stretch" に変更
    st.image("my_stock_analysis.png", width="stretch")