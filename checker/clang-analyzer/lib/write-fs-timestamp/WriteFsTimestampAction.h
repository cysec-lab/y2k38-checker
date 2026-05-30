#ifndef WRITE_FS_TIMESTAMP_ACTION_H
#define WRITE_FS_TIMESTAMP_ACTION_H

#include <memory>

#include "../Y2k38CheckBase.h"
#include "clang/AST/AST.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"

using namespace clang;
using namespace clang::ast_matchers;

namespace writefstimestamp {

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

inline void addMatcher(MatchFinder *Finder) {
    Finder->addMatcher(
        matcher,
        new y2k38::MatcherCallback<clang::DeclRefExpr>(ID, "y2k38 (write-fs-timestamp)"));
}

class WriteFsTimestampAction : public y2k38::ActionBase<WriteFsTimestampAction> {
   public:
    static void registerMatchers(clang::ast_matchers::MatchFinder *Finder) {
        addMatcher(Finder);
    }

    clang::PluginASTAction::ActionType getActionType() override {
        return ReplaceAction;
    }
};

}  // namespace writefstimestamp

#endif
