#ifndef WRITE_FS_TIMESTAMP_ACTION_H
#define WRITE_FS_TIMESTAMP_ACTION_H

#include <memory>

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
    declRefExpr(
        to(anyOf(functionDecl(hasName("utime"),
                              isExpansionInFileMatching("utime.h")),
                 functionDecl(hasName("utimes"),
                              isExpansionInFileMatching("sys/time.h")))))
        .bind(ID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        llvm::outs() << "[write file timestamp] ";
        if (const auto *declRefExpr =
                Result.Nodes.getNodeAs<clang::DeclRefExpr>(ID)) {
            SourceManager &sourceManager = *Result.SourceManager;
            SourceLocation loc = declRefExpr->getExprLoc();
            auto fileName = sourceManager.getFilename(loc);
            auto line = sourceManager.getSpellingLineNumber(loc);
            auto column = sourceManager.getSpellingColumnNumber(loc);
            llvm::outs() << "file: " << fileName << " : " << line << " : "
                         << column << "\n";
            // declRefExpr->dump();
        }
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

    clang::PluginASTAction::ActionType getActionType() override {
        return ReplaceAction;
    }
};

}  // namespace writefstimestamp

#endif
