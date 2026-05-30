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

using namespace clang;
using namespace clang::ast_matchers;

namespace writefstimestamp {

/**
 * Matcher
 */
static const char *ID = "write-fs-timestamp-id";
auto matcher =
    declRefExpr(to(anyOf(functionDecl(hasName("utime"),
                                      isExpansionInFileMatching("utime.h")),
                         functionDecl(hasName("utimes"),
                                      isExpansionInFileMatching("time.h")),
                         functionDecl(hasName("utimensat"),
                                      isExpansionInFileMatching("stat.h")),
                         functionDecl(hasName("futimes"),
                                      isExpansionInFileMatching("time.h")),
                         functionDecl(hasName("futimens"),
                                      isExpansionInFileMatching("stat.h")),
                         functionDecl(hasName("futimesat"),
                                      isExpansionInFileMatching("stat.h")),
                         functionDecl(hasName("lutimes"),
                                      isExpansionInFileMatching("time.h")))))
        .bind(ID);

// 定義ファイル指定ない版
// auto matcher =
//     declRefExpr(to(functionDecl(anyOf(hasName("utime"), hasName("utimes")))))
//         .bind(ID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        const auto *declRefExpr =
            Result.Nodes.getNodeAs<clang::DeclRefExpr>(ID);
        if (!declRefExpr) return;

        DiagnosticsEngine &DE = Result.Context->getDiagnostics();
        unsigned ID =
            DE.getCustomDiagID(DiagnosticsEngine::Warning,
                               "y2k38 (write-fs-timestamp)");
        DE.Report(declRefExpr->getBeginLoc(), ID);
    }
};

void addMatcher(MatchFinder *Finder) {
    MatcherCallback *matcherCallback = new MatcherCallback();
    Finder->addMatcher(matcher, matcherCallback);
}

class WriteFsTimestampAction : public clang::PluginASTAction {
   public:
    WriteFsTimestampAction() {}

    std::unique_ptr<clang::ASTConsumer> CreateASTConsumer(
        clang::CompilerInstance &ci, llvm::StringRef) override {
        clang::ast_matchers::MatchFinder *Finder = new clang::ast_matchers::MatchFinder();
        addMatcher(Finder);
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
