#ifndef READ_FS_TIMESTAMP_ACTION_H
#define READ_FS_TIMESTAMP_ACTION_H

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

namespace readfstimestamp {

/**
 * Matcher
 */
static const char *ID = "read-fs-timestamp-id";
auto matcher =
    memberExpr(member(anyOf(hasName("st_atim"), hasName("st_mtim"),
                            hasName("st_ctim"), hasName("st_atime"),
                            hasName("st_mtime"), hasName("st_ctime"))),
               has(declRefExpr(to(varDecl(hasType(asString("struct stat")))))))
        .bind(ID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        const auto *memberExpr = Result.Nodes.getNodeAs<clang::MemberExpr>(ID);
        if (!memberExpr) return;

        DiagnosticsEngine &DE = Result.Context->getDiagnostics();
        unsigned ID =
            DE.getCustomDiagID(DiagnosticsEngine::Warning,
                               "y2k38 (read-fs-timestamp)");
        DE.Report(memberExpr->getBeginLoc(), ID);
    }
};

void addMatcher(MatchFinder *Finder) {
    MatcherCallback *matcherCallback = new MatcherCallback();
    Finder->addMatcher(matcher, matcherCallback);
}

/**
 * Action
 */
class ReadFsTimestampAction : public clang::PluginASTAction {
   public:
    ReadFsTimestampAction() {}

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
        return AddAfterMainAction;
    }
};

}  // namespace readfstimestamp

#endif
