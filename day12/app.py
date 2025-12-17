import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import plotly.express as px # 新しく使うリッチなグラフライブラリ

# ページ設定
st.set_page_config(page_title="売上分析ダッシュボード", layout="wide")

st.title("📊 店舗・商品別 売上分析DXツール")
st.markdown("CSVデータをアップロードすると、自動で「重要指標」「トレンド」「ABC分析」を行います。")

# --- 1. データ読み込み ---
uploaded_file = st.sidebar.file_uploader("売上データ(CSV)をアップロード", type=["csv"])

if uploaded_file is None:
    st.info("👈 左側のサイドバーからCSVファイルをアップロードしてください。（テストデータを自動読み込みします）")
    try:
        df = pd.read_csv("day12/sales_data_dummy.csv")
    except:
        st.error("データがありません。generate_data.pyを実行してください。")
        st.stop()
else:
    df = pd.read_csv(uploaded_file)

# 日付変換
df["日付"] = pd.to_datetime(df["日付"])

# --- 2. KPI表示 ---
st.subheader("📈 全体サマリー")
col1, col2, col3, col4 = st.columns(4)

total_sales = df["売上金額"].sum()
total_qty = df["個数"].sum()
avg_price = df["単価"].mean()
n_products = df["商品名"].nunique()

col1.metric("総売上", f"¥{total_sales:,.0f}")
col2.metric("総販売数", f"{total_qty:,.0f} 個")
col3.metric("平均単価", f"¥{avg_price:,.0f}")
col4.metric("取扱商品数", f"{n_products} 種類")

st.markdown("---")

# --- 3. グラフエリア ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🏢 店舗別 売上構成")
    # Plotlyを使ったインタラクティブな円グラフ
    fig_pie = px.pie(df, values="売上金額", names="店舗", title="店舗ごとの売上シェア")
    st.plotly_chart(fig_pie, use_container_width=True)

with col_right:
    st.subheader("📅 月別 売上推移")
    # 月ごとに集計
    df["月"] = df["日付"].dt.strftime("%Y-%m")
    sales_by_month = df.groupby("月")["売上金額"].sum().reset_index()
    
    # Plotlyを使った棒グラフ
    fig_bar = px.bar(sales_by_month, x="月", y="売上金額", title="月次の売上トレンド")
    st.plotly_chart(fig_bar, use_container_width=True)

# --- 4. 【新機能】パレート分析 (ABC分析) ---
st.markdown("---")
st.subheader("🏆 商品別 パレート分析 (ABC分析)")
st.caption("売上の累積構成比に基づき、商品をランク付けします (A: 上位80% / B: 90% / C: その他)")

# 商品ごとに売上を集計して降順に並べる
df_pareto = df.groupby("商品名")["売上金額"].sum().sort_values(ascending=False).reset_index()

# 累積比率を計算
df_pareto["累積売上"] = df_pareto["売上金額"].cumsum()
df_pareto["累積比率"] = df_pareto["累積売上"] / df_pareto["売上金額"].sum()

# ABCクラス判定関数
def classify_abc(percentage):
    if percentage <= 0.8:
        return "A (主力商品)"
    elif percentage <= 0.9:
        return "B (準主力)"
    else:
        return "C (ロングテール)"

df_pareto["クラス"] = df_pareto["累積比率"].apply(classify_abc)

# グラフと表を表示
col_abc_graph, col_abc_table = st.columns([2, 1])

with col_abc_graph:
    # 色分けした棒グラフ
    fig_abc = px.bar(df_pareto, x="商品名", y="売上金額", color="クラス",
                     title="商品別売上とABCクラス分類",
                     color_discrete_map={"A (主力商品)": "blue", "B (準主力)": "green", "C (ロングテール)": "red"})
    st.plotly_chart(fig_abc, use_container_width=True)

with col_abc_table:
    st.write("ランク分け結果")
    st.dataframe(df_pareto[["商品名", "売上金額", "クラス"]], hide_index=True)