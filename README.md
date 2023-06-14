# y2k38-checker

## ディレクトリ構成

```sh
┗ clang-analyzer/ # 検出ツール
┗ build/          # clang-analyzer 用 build ディレクトリ
┗ clang-query/    # clang-query による AST dump ツール
┗ dataset/        # 解析対象の表現のある .c ファイル
┗ investigation/  # ソースコードクロール Python スクリプト
┗ log/            #
┗ out/            # ダウンロードした解析対象のソースコード
┗ run_all.py      # clang-analyzer を使用して out/* の C ファイルを解析する Python スクリプト
```

## 開発

1.  docker イメージの作成（初回のみ）

```
docker build . -t y2k38-checker:1
```

2. Docker image からコンテナを作成してログイン

```
sudo docker run -it y2k38-checker:1 bash
```

## 使用ソフトウェア

- [LLVM 11.0.0](https://github.com/llvm/llvm-project/releases/tag/llvmorg-11.0.0)
- Ubuntu 20.04
- Python 3.8.2

その他については [Dockerfile](./.DockerFile) を参照してください。
