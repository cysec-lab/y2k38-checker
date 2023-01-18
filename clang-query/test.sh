#!/bin/bash

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
run_clang_query \
    ./blacklist/read-fs-timestamp.matcher \
    ../dataset/blacklist/read-fs-timestamp.c


echo_title 'blacklist bug > write file timestamp'
run_clang_query \
    ./blacklist/write-fs-timestamp.matcher \
    ../dataset/blacklist/write-fs-timestamp.c


echo_title 'explicitly downcast bug'
run_clang_query \
    ./downcast-bug/exp-downcast.matcher \
    ../dataset/downcast-bug/exp-downcast.c


echo_title 'implicitly downcast bug > assign'
run_clang_query \
    ./downcast-bug/assign-imp-downcast.matcher \
    ../dataset/downcast-bug/assign-imp-downcast.c


echo_title 'implicitly downcast bug > return'
run_clang_query \
    ./downcast-bug/return-imp-downcast.matcher \
    ../dataset/downcast-bug/return-imp-downcast.c


echo_title 'implicitly downcast bug > func arg'
run_clang_query \
    ./downcast-bug/func-arg-imp-downcast.matcher \
    ../dataset/downcast-bug/func-arg-imp-downcast.c
