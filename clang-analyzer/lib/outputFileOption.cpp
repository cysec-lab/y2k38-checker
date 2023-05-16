#ifndef OUTPUT_FILE_OPTION_H
#define OUTPUT_FILE_OPTION_H

#include "clang/Frontend/CompilerInstance.h"

llvm::cl::opt<std::string> OutputFileOption(
    "y2k38-checker-output",
    llvm::cl::desc(
        "the json file to output detection results by y2k38 checker"));

#endif