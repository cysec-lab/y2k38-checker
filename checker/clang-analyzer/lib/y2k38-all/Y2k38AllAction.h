#ifndef Y2K38_ALL_ACTION_H
#define Y2K38_ALL_ACTION_H

#include <memory>

#include "clang/AST/AST.h"
#include "clang/AST/ASTConsumer.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"
#include "clang/Basic/Diagnostic.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendActions.h"
#include "clang/Tooling/Tooling.h"

#include "../read-fs-timestamp/ReadFsTimestampAction.h"
#include "../write-fs-timestamp/WriteFsTimestampAction.h"
#include "../timet-to-long-downcast/TimetToLongDowncast.h"
#include "../timet-to-int-downcast/TimetToIntDowncast.h"

using namespace clang;
using namespace clang::ast_matchers;

namespace y2k38all {


/**
 * Action
 */
class Y2k38AllAction : public clang::PluginASTAction {
   public:
    Y2k38AllAction() {}

    std::unique_ptr<clang::ASTConsumer> CreateASTConsumer(
        clang::CompilerInstance &ci, llvm::StringRef) override {
 
        clang::ast_matchers::MatchFinder *Finder = new clang::ast_matchers::MatchFinder();

        readfstimestamp::addMatcher(Finder);
        writefstimestamp::addMatcher(Finder);
        timet_to_long_downcast::addMatcher(Finder);
        timet_to_int_downcast::addMatcher(Finder);
 
        return Finder->newASTConsumer();
    }

    bool ParseArgs(const clang::CompilerInstance &ci,
                   const std::vector<std::string> &args) override {
        return true;
    }

    clang::PluginASTAction::ActionType getActionType() override {
        return AddAfterMainAction;
    }
};

}  // namespace y2k38all

#endif
