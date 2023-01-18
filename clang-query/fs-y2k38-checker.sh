#!/bin/bash

# 解析対象のファイル
FILE=`pwd`/$1

# 実行ファイルのあるディレクトリに移動
cd `dirname $0`


run_clang_query(){
    # run_clang_query <matcher> <file>
    clang-query --extra-arg=-w -f $1 $2 --
}

echo_title(){
    echo "\n\n\n"
    echo ==========================================================================================
    echo $1
    echo ==========================================================================================
}


echo_title 'blacklist bug > read file timestamp'
run_clang_query ./blacklist/read-fs-timestamp.matcher ${FILE}

echo_title 'blacklist bug > write file timestamp'
run_clang_query ./blacklist/write-fs-timestamp.matcher ${FILE}

echo_title 'explicitly downcast bug'
run_clang_query ./downcast-bug/exp-downcast.matcher ${FILE}

echo_title 'implicitly downcast bug > assign'
run_clang_query ./downcast-bug/assign-imp-downcast.matcher ${FILE}

echo_title 'implicitly downcast bug > return'
run_clang_query ./downcast-bug/return-imp-downcast.matcher ${FILE}

echo_title 'implicitly downcast bug > func arg'
run_clang_query ./downcast-bug/func-arg-imp-downcast.matcher ${FILE}