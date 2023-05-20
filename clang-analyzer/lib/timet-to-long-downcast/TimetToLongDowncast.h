#ifndef TIMET_TO_LONG_DOWNCAST_ACTION_H
#define TIMET_TO_LONG_DOWNCAST_ACTION_H

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

using namespace clang;
using namespace clang::ast_matchers;

namespace timet_to_long_downcast {

/**
 * time_t 相当判定関数
 */
bool isTimeTEquivalent(const clang::Expr *expr) {
    if (const ParenExpr *parenExpr = dyn_cast<ParenExpr>(expr)) {
        return isTimeTEquivalent(parenExpr->getSubExpr());
    }
    if (expr->getType().getAsString() == "time_t" ||
        expr->getType().getAsString() == "__time_t") {
        return true;
    }
    // BinaryOperatorであれば再帰的に確認
    if (const BinaryOperator *binaryOperator = dyn_cast<BinaryOperator>(expr)) {
        return isTimeTEquivalent(binaryOperator->getLHS()) ||
               isTimeTEquivalent(binaryOperator->getRHS());
    }
    return false;
};

/**
 * Matcher
 */
static const char *ID = "time_t-to-long-downcast-id";
auto matcher = castExpr(anyOf(  // キャスト式
                            hasType(asString("long")), has(expr()),  // 通常
                            hasParent(binaryOperator(
                                isAssignmentOperator(),
                                hasType(asString("long"))))  // 演算代入演算子
                            ))
                   .bind(ID);
// auto matcher = castExpr(                      // キャスト式
//                    hasType(asString("long")),  // long 型へのキャスト
//                    has(expr())                // time_t 型へのキャスト
//                    )
//                    .bind(ID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
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

            const std::string type = "timet-to-long-downcast";
            llvm::outs() << "[" << type << "] " << file.path << ":" << file.line
                         << ":" << file.column << "\n";

            if (!OutputFileOption.empty()) {
                writeJsonFile(OutputFileOption, {
                    type : type,
                    file : file.path,
                    line : file.line,
                    column : file.column
                });
            }
        }
    }
};

/**
 * Action
 */
class TimetToLongDowncastAction : public clang::PluginASTAction {
   public:
    TimetToLongDowncastAction() {}

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

}  // namespace timet_to_long_downcast

#endif
