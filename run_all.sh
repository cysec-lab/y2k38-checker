#!/bin/bash

cd out/

date=$(date '+%Y-%m-%d-%H:%M:%S')
log_file="/home/cysec/develop/y2k38-checker/log/$date.log"
touch "$log_file"
echo "touched " $log_file "\n"

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
class MatcherCallback : public clang::ast_matchers::MatchFinder::Matc