# 1. ベースイメージの指定（Python 3.11 を使う）
FROM python:3.11-slim

# 2. コンテナ内の作業ディレクトリを設定
WORKDIR /app

# 3. 必要なパッケージをインストールするためにOSの更新
# (gitなどはStreamlitの動作に必要になることがあるため入れておくと安全)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# 4. ローカルの requirements.txt をコンテナにコピー
COPY requirements.txt .

# 5. Pythonライブラリのインストール
RUN pip install --no-cache-dir -r requirements.txt

# 6. アプリケーションのコードをすべてコンテナにコピー
COPY . .

# 7. Streamlitが使うポート（8501）を開ける
EXPOSE 8501

# 8. コンテナ起動時に実行するコマンド
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]