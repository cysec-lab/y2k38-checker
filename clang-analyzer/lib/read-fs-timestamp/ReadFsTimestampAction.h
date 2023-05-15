#ifndef READ_FS_TIMESTAMP_ACTION_H
#define READ_FS_TIMESTAMP_ACTION_H

#include <memory>

#include "../writeJsonFile.h"
#include "clang/AST/AST.h"
#include "clang/AST/ASTConsumer.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"
#include "clang/Basic/Diagnostic.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendActions.h"
#include "clang/Tooling/Tooling.h"

namespace readfstimestamp {

/**
 * Matcher
 */
using namespace clang;
using namespace clang::ast_matchers;
static const char *ID = "read-fs-timestamp-id";
auto matcher =
    memberExpr(member(anyOf(hasName("st_atim"), hasName("st_mtim"),
                            hasName("st_ctim"))),
               has(declRefExpr(to(varDecl(hasType(asString("struct stat")))))))
        .bind(ID);

class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   private:
    std::vector<MatchedAst> matchedAst;

   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        if (const auto *memberExpr =
                Result.Nodes.getNodeAs<clang::MemberExpr>(ID)) {
            const clang::SourceLocation loc = memberExpr->getBeginLoc();
            llvm::SmallString<128> absFilePath(
                Result.SourceManager->getFilename(loc).str());
            Result.SourceManager->getFileManager().makeAbsolutePath(
                absFilePath);
            const unsigned int line =
                Result.SourceManager->getSpellingLineNumber(loc);
            const unsigned int column =
                Result.SourceManager->getSpellingColumnNumber(loc);

            std::string type = "read-file-timestamp";
            llvm::outs() << "[" << type << "] " << absFilePath << ":" << line
                         << ":" << column << "\n";

            writeJsonFile({
                file : absFilePath.str(),
                type : type,
                line : static_cast<int>(line),
                column : static_cast<int>(column)
            });
        }
    }
};

/**
 * Action
 */
class ReadFsTimestampAction : public clang::PluginASTAction {
   public:
    ReadFsTimestampAction() {}

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

}  // namespace readfstimestamp

#endif
