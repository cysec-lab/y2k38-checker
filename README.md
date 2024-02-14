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
code y2k38-checker/
```

## detector/clang-analyzer

検出ツール

### ビルド

## detector/clang-query

clang-query による AST dump ツール

## dataset

## investigation

各論文での調査用スクリプト。
詳細は各ディレクトリの README.md を参照してください。
