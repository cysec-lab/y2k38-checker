#!/bin/bash

cd out/

log_file="/home/cysec/develop/y2k38-checker/test.log"
echo "\n\n $(date) ===========================================" >>"$log_file"

for entry in "$(pwd)"/*/; do
    dirname="${entry%/}" # 末尾のスラッシュを削除
    echo "$dirname"
    echo "\n" "$dirname" >>"$log_file"

    # 初期化
    echo "[]" >"$dirname"/analyzed.json

    /home/cysec/develop/y2k38-checker/build/bin/check-y2k38 \
        -p $dirname/compile_commands.json \
        -y2k38-checker-output $dirname/analyzed.json \
        >>"$log_file"
done

cd ../
