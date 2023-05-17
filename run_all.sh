#!/bin/bash
cd out/

for entry in "$(pwd)"/*/; do
    dirname="${entry%/}" # 末尾のスラッシュを削除

    echo "analyze: " "$dirname"

    # 初期化
    echo "[]" >"$dirname"/analyzed.json

    sh "$dirname"/run.sh

    echo "\n"
done

cd ../
