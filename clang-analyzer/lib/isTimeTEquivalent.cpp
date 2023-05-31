#ifndef IS_TIMET_EQUIVALENT_H
#define IS_TIMET_EQUIVALENT_H

#include "clang/AST/AST.h"

using namespace clang;

/**
 * time_t 相当判定関数
 */
bool isTimeTEquivalent(const clang::Expr *expr) {
    if (expr->getType().getAsString() == "time_t" ||
        expr->getType().getAsString() == "__time_t") {
        return true;
    }
    if (const ParenExpr *parenExpr = dyn_cast<ParenExpr>(expr)) {
        return isTimeTEquivalent(parenExpr->getSubExpr());
    }
    // BinaryOperatorであれば再帰的に確認
    if (const BinaryOperator *binaryOperator = dyn_cast<BinaryOperator>(expr)) {
        return isTimeTEquivalent(binaryOperator->getLHS()) ||
               isTimeTEquivalent(binaryOperator->getRHS());
    }
    return false;
};

#endif
