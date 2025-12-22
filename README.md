# Stock Analysis Tool 📈

## 概要
Pythonを用いて株価データを自動取得し、テクニカル分析（SMA, RSI）を行った上で、その結果を可視化するツールです。
金融データ分析の基礎的なワークフロー（データ取得・加工・分析・可視化）を自動化するために作成しました。

## 機能
* **データ取得**: `yfinance` ライブラリを使用し、指定した銘柄（例: Apple）の株価データを取得。
* **テクニカル分析**:
    * 単純移動平均線 (SMA: Simple Moving Average) の算出
    * 相対力指数 (RSI: Relative Strength Index) の算出
* **可視化**: 分析結果をグラフ化し、画像ファイルとして保存。

## 使用技術 (Tech Stack)
* **Language**: Python 3.x
* **Data Analysis**: pandas, numpy
* **Visualization**: matplotlib
* **Data Source**: yfinance
* **Environment**: Docker, VS Code

## インストールと実行方法

1. 必要なライブラリをインストールします。
   ```bash
   pip install -r requirements.txt
   python generate_chart.py