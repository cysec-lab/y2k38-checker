#ifndef Y2K38_CHECKER_ACTION_H
#define Y2K38_CHECKER_ACTION_H

#include <memory>

#include "clang/AST/AST.h"
#include "clang/AST/ASTConsumer.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"
#include "clang/Basic/Diagnostic.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendActions.h"
#include "clang/Tooling/Tooling.h"

/**
 * Matcher
 */
using namespace clang::ast_matchers;
static const char *FunctionID = "function-id";
clang::ast_matchers::DeclarationMatcher matcher =
    functionDecl().bind(FunctionID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        llvm::outs() << "[found] ";
        if (const auto *F =
                Result.Nodes.getNodeAs<clang::FunctionDecl>(FunctionID)) {
            const auto &SM = *Result.SourceManager;
            const auto &Loc = F->getLocation();
            llvm::outs() << SM.getFilename(Loc) << ":"
                         << SM.getSpellingLineNumber(Loc) << ":"
                         << SM.getSpellingColumnNumber(Loc) << "\n";
        }
    }
};

namespace y2k38checker {

class Y2k38CheckerAction : public clang::PluginASTAction {
   public:
    Y2k38CheckerAction() {}

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

}  // namespace y2k38checker

#endif
