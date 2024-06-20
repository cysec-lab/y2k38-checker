REPOSITORY_PATH = "/home/cysec/develop/y2k38-checker"

BUILD_PATH = REPOSITORY_PATH + "/build"

LIBRARY_PATHS_READ_FS_TIMESTAMP = BUILD_PATH + "/lib/libread-fs-timestamp-plugin.so"
LIBRARY_PATHS_WRITE_FS_TIMESTAMP = BUILD_PATH + "/lib/libwrite-fs-timestamp-plugin.so"
LIBRARY_PATHS_TIME_T_TO_INT = BUILD_PATH + "/lib/libtimet-to-int-downcast-plugin.so"
LIBRARY_PATHS_TIME_T_TO_LONG = BUILD_PATH + "/lib/libtimet-to-long-downcast-plugin.so"

DATASET_PATHS_READ_FS_TIMESTAMP = REPOSITORY_PATH + "/dataset/blacklist/read-fs-timestamp.c"
DATASET_PATHS_WRITE_FS_TIMESTAMP = REPOSITORY_PATH + "/dataset/blacklist/write-fs-timestamp.c"
DATASET_PATHS_ASSIGN_IMP_DOWNCAST = REPOSITORY_PATH + "/dataset/downcast-bug/assign-imp-downcast.c"
DATASET_PATHS_EXP_DOWNCAST = REPOSITORY_PATH + "/dataset/downcast-bug/exp-downcast.c"
DATASET_PATHS_FUNC_ARG_IMP_DOWNCAST = REPOSITORY_PATH + "/dataset/downcast-bug/func-arg-imp-downcast.c"
DATASET_PATHS_RETURN_IMP_DOWNCAST = REPOSITORY_PATH + "/dataset/downcast-bug/return-imp-downcast.c"

CLANG_COMMAND = REPOSITORY_PATH + "/clang+llvm-11.0.0-x86_64-linux-gnu-ubuntu-20.04/bin/clang"
