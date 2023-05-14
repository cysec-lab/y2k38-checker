#ifndef EXPLICIT_DOWNCAST_ACTION_H
#define EXPLICIT_DOWNCAST_ACTION_H

#include <memory>

#include "clang/AST/AST.h"
#include "clang/AST/ASTConsumer.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"
#include "clang/Basic/Diagnostic.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendActions.h"
#include "clang/Tooling/Tooling.h"

namespace explicitdowncast {

using namespace clang;
using namespace clang::ast_matchers;

/**
 * time_t 相当判定関数
 */
bool isTimeTEquivalent(const clang::Expr *expr) {
    expr->dump();
    llvm::outs() << "\n\n";
    if (expr->getType().getAsString() == "time_t") {
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
static const char *ID = "explicit-downcast-id";
auto matcher = castExpr(hasType(asString("int")), has(expr())).bind(ID);

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

            llvm::outs() << "[explicit downcast] ";
            SourceManager &sourceManager = *Result.SourceManager;
            SourceLocation loc = castExpr->getBeginLoc();
            auto fileName = sourceManager.getFilename(loc);
            auto line = sourceManager.getSpellingLineNumber(loc);
            auto column = sourceManager.getSpellingColumnNumber(loc);
            llvm::outs() << "file: " << fileName << " : " << line << " : "
                         << column << "\n";
        }

    }  // namespace explicitdowncast
};

class ExplicitDowncastAction : public clang::PluginASTAction {
   public:
    ExplicitDowncastAction() {}

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

}  // namespace explicitdowncast

#endif
