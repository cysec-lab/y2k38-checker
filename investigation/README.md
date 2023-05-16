# 検証

以下の処理を行う Python スクリプト

1. GitHub からソースコードをダウンロード
2. 検出ツールの入力に与える `compile_commands.json` を生成
3. 検出ツールを実行するシェルスクリプトを作成

## 準備

- Python 3.9.6 を用意
- setting.py の `_REPO` をローカル環境に合わせて書き換える

## 実行

```sh
py investigation/preprocess.py
```

## 生成されるディレクトリの構成

```sh
┗ ...
┗ out/
    ┗ [project_repository]/
		┗ [project_repository].zip  # ダウンロードした zipファイル
		┗ src/                      # zip解凍済みソースファイル
		┗ compile_commands.json     # 検出ツールへの入力ファイル
		┗ analyzed.json             # 検出結果
		┗ run.sh                    # 検出ツール実行
```
