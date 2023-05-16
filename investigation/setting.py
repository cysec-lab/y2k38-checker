_REPO = "/home/cysec/develop/y2k38-checker"
OUT_DIR             = _REPO + "/out"
CLANG_PATH          = _REPO + "/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang"
TOOL_RUN_DIRECTORY  = _REPO + "/build"
TOOL_PATH           = _REPO + "/build/bin/check-y2k38"

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