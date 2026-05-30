#ifndef TIMET_TO_LONG_DOWNCAST_ACTION_H
#define TIMET_TO_LONG_DOWNCAST_ACTION_H

#include <memory>

#include "../isTimeTEquivalent.cpp"
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

namespace timet_to_long_downcast {

/**
 * Matcher
 */
static const char *ID = "to-long-cast-id";

// time_t判定関数を使わない場合の調査用
// auto timetExpr =
//     expr(anyOf(hasType(asString("time_t")), hasType(asString("__time_t"))));

// longへのキャスト
auto toLongCastExprMatcher =
    castExpr(hasType(asString("long")), has(expr())).bind(ID);

// 演算代入演算子
auto assignmentOperatorMatcher =
    binaryOperator(isAssignmentOperator(), hasType(asString("long")),
                   has(expr()))
        .bind(ID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        const auto *castExpr = Result.Nodes.getNodeAs<clang::Expr>(ID);
        if (!castExpr) return;

        DiagnosticsEngine &DE = Result.Context->getDiagnostics();
        unsigned ID =
            DE.getCustomDiagID(DiagnosticsEngine::Warning,
                               "y2k38 (timet-to-long-downcast)");
        DE.Report(castExpr->getBeginLoc(), ID);    }
};

void addMatcher(MatchFinder *Finder) {
    MatcherCallback *matcherCallback = new MatcherCallback();
    Finder->addMatcher(toLongCastExprMatcher, matcherCallback);
    Finder->addMatcher(assignmentOperatorMatcher, matcherCallback);
}

/**
 * Action
 */
class TimetToLongDowncastAction : public clang::PluginASTAction {
   public:
    TimetToLongDowncastAction() {}

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

}  // namespace timet_to_long_downcast

#endif
