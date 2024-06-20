# y2k38-checker

## 環境構築

前提

- VSCode がインストールされていること
- Docker/Docker Compose がインストールされていること
- Git がインストールされていること

Docker 環境推奨ですが、もしローカルに構築する場合は[Dockerfile](./Dockerfile)を参照してください。

1. git clone
2. volume mount 用ディレクトリの作成
3. VSCode ワークスペースの起動
4. Dev Container の起動。
   コマンドパレット（`cmd ⌘` + shift + `P`）で `devcontainers: rebuild and Reopen in Container`を選択

```sh
git clone https://github.com/cysec-lab/y2k38-checker.git
mkdir .y2k38-checker # volume mount用ディレクトリの作成

```

## ディレクトリ構成

```sh
.
├── README.md
├── .devcontainer
├── checker # 検出ツール
│   ├── clang-analyzer # clang-analyzer 製（最新版）
│   ├── clang-query # clang-query 製（卒論版）
├── dataset # 2038年問題を抱えるプログラム例
├── investigation # 検証プログラム
     ├── dicomo # DICOMO2023、2023年5月検証実施
     ├── ipsj-embebbed # 情報処理学会ジャーナル 組込みシステム特集、2023年11月検証実施
```
