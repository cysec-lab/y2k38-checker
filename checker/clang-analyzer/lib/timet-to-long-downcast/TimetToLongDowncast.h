#ifndef TIMET_TO_LONG_DOWNCAST_ACTION_H
#define TIMET_TO_LONG_DOWNCAST_ACTION_H

#include <memory>

#include "../Y2k38CheckBase.h"
#include "../isTimeTEquivalent.cpp"
#include "clang/AST/AST.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"

using namespace clang;
using namespace clang::ast_matchers;

namespace timet_to_long_downcast {

static const char *ID = "to-long-cast-id";

auto toLongCastExprMatcher =
    castExpr(hasType(asString("long")), has(expr())).bind(ID);

auto assignmentOperatorMatcher =
    binaryOperator(isAssignmentOperator(), hasType(asString("long")),
                   has(expr()))
        .bind(ID);

inline void addMatcher(MatchFinder *Finder) {
    auto *cb = new y2k38::MatcherCallback<clang::Expr>(ID, "y2k38 (timet-to-long-downcast)");
    Finder->addMatcher(toLongCastExprMatcher, cb);
    Finder->addMatcher(assignmentOperatorMatcher, cb);
}

class TimetToLongDowncastAction : public y2k38::ActionBase<TimetToLongDowncastAction> {
   public:
    static void registerMatchers(clang::ast_matchers::MatchFinder *Finder) {
        addMatcher(Finder);
    }

    clang::PluginASTAction::ActionType getActionType() override {
        return ReplaceAction;
    }
};

}  // namespace timet_to_long_downcast

#endif
