
project(y2k38-clang-analyzer-tests)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_library(testlib
  files.c
  functions.c
)

