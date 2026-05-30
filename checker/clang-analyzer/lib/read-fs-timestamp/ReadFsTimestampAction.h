#ifndef READ_FS_TIMESTAMP_ACTION_H
#define READ_FS_TIMESTAMP_ACTION_H

#include <memory>

#include "../Y2k38CheckBase.h"
#include "clang/AST/AST.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"

using namespace clang;
using namespace clang::ast_matchers;

namespace readfstimestamp {

static const char *ID = "read-fs-timestamp-id";
auto matcher =
    memberExpr(member(anyOf(hasName("st_atim"), hasName("st_mtim"),
                            hasName("st_ctim"), hasName("st_atime"),
                            hasName("st_mtime"), hasName("st_ctime"))),
               has(declRefExpr(to(varDecl(hasType(asString("struct stat")))))))
        .bind(ID);

inline void addMatcher(MatchFinder *Finder) {
    Finder->addMatcher(
        matcher,
        new y2k38::MatcherCallback<clang::MemberExpr>(ID, "y2k38 (read-fs-timestamp)"));
}

class ReadFsTimestampAction : public y2k38::ActionBase<ReadFsTimestampAction> {
   public:
    static void registerMatchers(clang::ast_matchers::MatchFinder *Finder) {
        addMatcher(Finder);
    }

    clang::PluginASTAction::ActionType getActionType() override {
        return AddAfterMainAction;
    }
};

}  // namespace readfstimestamp

#endif
