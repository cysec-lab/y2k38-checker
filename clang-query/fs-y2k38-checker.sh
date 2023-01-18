#!/bin/bash

# 解析対象のファイル
FILE=$(pwd)/$1

# 実行ファイルのあるディレクトリに移動
cd "$(dirname "$0")" || exit

echo_red() {
    printf '\033[31m%s\033[m\n' "$1"
}

run_clang_query() {
    # run_clang_query <matcher> <file> <title>
    message=$(clang-query --extra-arg=-w -f "$1" "$2" --)

    NO_MATCHED_MSG="0 matches."

    if [ "$message" != "$NO_MATCHED_MSG" ]; then
        echo_red "[WARNING]: $3"
        echo "$message"
        printf "\n\n\n"
    else
        echo "[OK]: $3"
    fi
}

run_clang_query ./blacklist/read-fs-timestamp.matcher "${FILE}" 'blacklist bug > read file timestamp'

run_clang_query ./blacklist/write-fs-timestamp.matcher "${FILE}" 'blacklist bug > write file timestamp'

run_clang_query ./downcast-bug/exp-downcast.matcher "${FILE}" 'explicitly downcast bug'

run_clang_query ./downcast-bug/assign-imp-downcast.matcher "${FILE}" 'implicitly downcast bug > assign'

run_clang_query ./downcast-bug/return-imp-downcast.matcher "${FILE}" 'implicitly downcast bug > return'

run_clang_query ./downcast-bug/func-arg-imp-downcast.matcher "${FILE}" 'implicitly downcast bug > func arg'
