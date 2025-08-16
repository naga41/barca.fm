# 開発環境セットアップ手順

このドキュメントは、このリポジトリで開発を行うための環境構築手順をまとめたものです。

## 1. リポジトリのクローン

```bash
git clone https://github.com/naga41/barca.fm.git
cd barca.fm
```

## 2. Python仮想環境の作成と有効化

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. 依存ライブラリのインストール

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

## 4. テーマのインストール

`pelican-clean-blog` テーマをクローンし、インストールします。

```bash
git clone https://github.com/gilsondev/pelican-clean-blog.git
venv/bin/pelican-themes --install ./pelican-clean-blog
```

## 5. 開発サーバーの起動

以下のコマンドで開発サーバーを起動します。

```bash
make devserver PELICAN=venv/bin/pelican
```

## 6. サイトの確認

ブラウザで `http://localhost:8000` にアクセスし、サイトが表示されることを確認してください。
