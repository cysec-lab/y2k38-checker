#ifndef TIMET_TO_INT_DOWNCAST_ACTION_H
#define TIMET_TO_INT_DOWNCAST_ACTION_H

#include <memory>

#include "../absoluteFilePath.cpp"
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

namespace timet_to_int_downcast {

/**
 * Matcher
 */
static const char *ID = "to-int-cast-id";

// time_t判定関数を使わない場合の調査用
// auto timetExpr =
//     expr(anyOf(hasType(asString("time_t")), hasType(asString("__time_t"))));

// intへのキャスト
auto toIntCastExprMatcher =
    castExpr(hasType(asString("int")), has(expr())).bind(ID);

// 演算代入演算子
auto assignmentOperatorMatcher =
    binaryOperator(isAssignmentOperator(), hasType(asString("int")),
                   has(expr()))
        .bind(ID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   private:
    void printPath(file_s &file) {
        const std::string type = "timet-to-int-downcast";
        llvm::outs() << "[" << type << "] " << file.path << ":" << file.line
                     << ":" << file.column << "\n";
    }

   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        const auto *castExpr = Result.Nodes.getNodeAs<clang::Expr>(ID);

        if (!castExpr) return;

        for (clang::Expr::const_child_iterator it = castExpr->child_begin();
             it != castExpr->child_end(); ++it) {
            const clang::Expr *childExpr = clang::dyn_cast<clang::Expr>(*it);
            if (!childExpr) continue;
            if (!isTimeTEquivalent(childExpr)) continue;

            file_s file = exprAbsoluteFilePath(castExpr, Result);
            printPath(file);
        }
    }
};

/**
 * Action
 */
class TimetToIntDowncastAction : public clang::PluginASTAction {
   public:
    TimetToIntDowncastAction() {}

    std::unique_ptr<clang::ASTConsumer> CreateASTConsumer(
        clang::CompilerInstance &ci, llvm::StringRef) override {
        ci.getDiagnostics().setClient(new clang::IgnoringDiagConsumer());

        MatcherCallback *matcherCallback = new MatcherCallback();
        clang::ast_matchers::MatchFinder *Finder =
            new clang::ast_matchers::MatchFinder();
        Finder->addMatcher(toIntCastExprMatcher, matcherCallback);
        Finder->addMatcher(assignmentOperatorMatcher, matcherCallback);
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

}  // namespace timet_to_int_downcast

#endif
