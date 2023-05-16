OUT_DIR = "/home/cysec/develop/y2k38-checker/out"

# compile_commands.json 用
CLANG_PATH = "/home/cysec/develop/y2k38-checker/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang"
TOOL_RUN_DIRECTORY = "/home/cysec/develop/y2k38-checker/build"
TOOL_PATH = "/home/cysec/develop/y2k38-checker/build/bin/check-y2k38"

TARGET_ZIP_URLS = [
    { 
        "name": "krakjoe-phpdbg", 
        "url":  "https://github.com/krakjoe/phpdbg/archive/refs/heads/master.zip" 
    },
    {
        "name":"karthick18-inception",
        "url":"https://github.com/karthick18/inception/archive/refs/heads/master.zip"
    }
]