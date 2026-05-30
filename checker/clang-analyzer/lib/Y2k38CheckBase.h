#ifndef Y2K38_CHECK_BASE_H
#define Y2K38_CHECK_BASE_H

#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/Basic/Diagnostic.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendActions.h"

namespace y2k38 {

/**
 * Shared MatchFinder callback: looks up NodeType by id and emits a warning.
 */
template <typename NodeType>
class MatcherCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
    const char *id_;
    const char *category_;

   public:
    MatcherCallback(const char *id, const char *category)
        : id_(id), category_(category) {}

    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult &Result) final {
        const auto *node = Result.Nodes.getNodeAs<NodeType>(id_);
        if (!node) return;

        clang::DiagnosticsEngine &DE = Result.Context->getDiagnostics();
        unsigned diagID = DE.getCustomDiagID(
            clang::DiagnosticsEngine::Warning, category_);
        DE.Report(node->getBeginLoc(), diagID);
    }
};

/**
 * CRTP base for single-check PluginASTActions.
 * Derived must provide: static void registerMatchers(MatchFinder *)
 */
template <typename Derived>
class ActionBase : public clang::PluginASTAction {
   public:
    std::unique_ptr<clang::ASTConsumer> CreateASTConsumer(
        clang::CompilerInstance &ci, llvm::StringRef) override {
        auto *Finder = new clang::ast_matchers::MatchFinder();
        Derived::registerMatchers(Finder);
        return Finder->newASTConsumer();
    }

    bool ParseArgs(const clang::CompilerInstance &ci,
                   const std::vector<std::string> &args) override {
        return true;
    }
};

}  // namespace y2k38

#endif
