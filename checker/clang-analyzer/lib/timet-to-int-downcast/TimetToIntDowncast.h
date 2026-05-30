#ifndef TIMET_TO_INT_DOWNCAST_ACTION_H
#define TIMET_TO_INT_DOWNCAST_ACTION_H

#include <memory>

#include "../Y2k38CheckBase.h"
#include "../isTimeTEquivalent.cpp"
#include "clang/AST/AST.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"

using namespace clang;
using namespace clang::ast_matchers;

namespace timet_to_int_downcast {

static const char *ID = "to-int-cast-id";

auto toIntCastExprMatcher =
    castExpr(hasType(asString("int")), has(expr())).bind(ID);

auto assignmentOperatorMatcher =
    binaryOperator(isAssignmentOperator(), hasType(asString("int")),
                   has(expr()))
        .bind(ID);

inline void addMatcher(MatchFinder *Finder) {
    auto *cb = new y2k38::MatcherCallback<clang::Expr>(ID, "y2k38 (timet-to-int-downcast)");
    Finder->addMatcher(toIntCastExprMatcher, cb);
    Finder->addMatcher(assignmentOperatorMatcher, cb);
}

class TimetToIntDowncastAction : public y2k38::ActionBase<TimetToIntDowncastAction> {
   public:
    static void registerMatchers(clang::ast_matchers::MatchFinder *Finder) {
        addMatcher(Finder);
    }

    clang::PluginASTAction::ActionType getActionType() override {
        return ReplaceAction;
    }
};

}  // namespace timet_to_int_downcast

#endif
