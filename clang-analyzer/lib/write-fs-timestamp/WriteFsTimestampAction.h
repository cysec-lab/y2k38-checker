#ifndef WRITE_FS_TIMESTAMP_ACTION_H
#define WRITE_FS_TIMESTAMP_ACTION_H

#include <memory>

#include "../absoluteFilePath.cpp"
#include "../outputFileOption.cpp"
#include "../writeJsonFile.cpp"
#include "clang/AST/AST.h"
#include "clang/AST/ASTConsumer.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"
#include "clang/Basic/Diagnostic.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendActions.h"
#include "clang/Tooling/Tooling.h"

namespace writefstimestamp {

/**
 * Matcher
 */
using namespace clang;
using namespace clang::ast_matchers;
static const char *ID = "write-fs-timestamp-id";
auto matcher =
    declRefExpr(to(anyOf(functionDecl(hasName("utime"),
                                      isExpansionInFileMatching("utime.h")),
                         functionDecl(hasName("utimes"),
                                      isExpansionInFileMatching("time.h")))))
        .bind(ID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        const auto *declRefExpr =
            Result.Nodes.getNodeAs<clang::DeclRefExpr>(ID);
        if (!declRefExpr) return;

        file_s file = exprAbsoluteFilePath(declRefExpr, Result);

        const std::string type = "write-fs-timestamp";
        llvm::outs() << "[" << type << "] " << file.path << ":" << file.line
                     << ":" << file.column << "\n";
        writeJsonFile(OutputFileOption, {
            type : type,
            file : file.path,
            line : file.line,
            column : file.column
        });
    }
};

class WriteFsTimestampAction : public clang::PluginASTAction {
   public:
    WriteFsTimestampAction() {}

    std::unique_ptr<clang::ASTConsumer> CreateASTConsumer(
        clang::CompilerInstance &ci, llvm::StringRef) override {
        ci.getDiagnostics().setClient(new clang::IgnoringDiagConsumer());

        MatcherCallback *matcherCallback = new MatcherCallback();
        clang::ast_matchers::MatchFinder *Finder =
            new clang::ast_matchers::MatchFinder();
        Finder->addMatcher(matcher, matcherCallback);
        return Finder->newASTConsumer();
    }

    bool ParseArgs(const clang::CompilerInstance &ci,
                   const std::vector<std::string> &args) override {
        return true;
    }

    bool BeginSourceFileAction(CompilerInstance &CI) override {
        if (OutputFileOption.empty()) {
            llvm::errs() << "[error] option -" << OutputFileOption.ArgStr
                         << " must be required.\n";
            std::exit(1);
        }
        return true;
    }

    clang::PluginASTAction::ActionType getActionType() override {
        return ReplaceAction;
    }
};

}  // namespace writefstimestamp

#endif
