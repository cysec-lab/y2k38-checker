#ifndef RELATIVE_TO_ABSOLUTE_PATH_H
#define RELATIVE_TO_ABSOLUTE_PATH_H

#include <llvm/ADT/StringRef.h>
#include <llvm/Support/Path.h>

#include "clang/AST/AST.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/Tooling/Tooling.h"

using namespace clang;

struct file_s {
    std::string path;
    unsigned int line;
    unsigned int column;
};

/**
 * MatchResult から ソースコードの絶対パスと行:列を取得する
 */
file_s exprAbsoluteFilePath(
    const clang::Expr* expr,
    const clang::ast_matchers::MatchFinder::MatchResult& Result) {
    SourceLocation loc = expr->getBeginLoc();

    llvm::SmallString<256> absolutePath(
        Result.SourceManager->getFilename(loc).str());
    Result.SourceManager->getFileManager().makeAbsolutePath(absolutePath);
    llvm::sys::path::remove_dots(absolutePath,
                                 /*remove_dot_dot=*/true);
    llvm::sys::path::remove_leading_dotslash(absolutePath);
    std::string path(absolutePath.str().data(), absolutePath.str().size());

    const unsigned int line = Result.SourceManager->getSpellingLineNumber(loc);
    const unsigned int column =
        Result.SourceManager->getSpellingColumnNumber(loc);

    file_s file{path : path, line : line, column : column};
    return file;
};

#endif