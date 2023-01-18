#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"
#include "clang/Frontend/FrontendActions.h"
#include "clang/Frontend/FrontendPluginRegistry.h"
#include "clang/Frontend/TextDiagnosticPrinter.h"
#include "clang/Rewrite/Core/Rewriter.h"
#include "clang/Tooling/CommonOptionsParser.h"
#include "clang/Tooling/Tooling.h"
#include "llvm/Support/CommandLine.h"
#include "llvm/Support/Signals.h"

using namespace clang::ast_matchers;

static const char* FunctionID = "function-id";
clang::ast_matchers::DeclarationMatcher M = functionDecl(
    decl().bind(FunctionID),
    hasAnyParameter(hasType(recordDecl(matchesName("std::vector")))));

class VecCallback : public clang::ast_matchers::MatchFinder::MatchCallback {
   public:
    virtual void run(
        const clang::ast_matchers::MatchFinder::MatchResult& Result) final {
        llvm::outs() << ".";
        // if (const auto* F =
        //         Result.Nodes.getDeclAs<clang::FunctionDecl>(FunctionID)) {
        //     const auto& SM = *Result.SourceManager;
        //     const auto& Loc = F->getLocation();
        //     llvm::outs() << SM.getFilename(Loc) << ":"
        //                  << SM.getSpellingLineNumber(Loc) << ":"
        //                  << SM.getSpellingColumnNumber(Loc) << "\n";
        // }
    }
};

static llvm::cl::OptionCategory FindVecCategory("find-vec options");

static llvm::cl::extrahelp CommonHelp(
    clang::tooling::CommonOptionsParser::HelpMessage);

static llvm::cl::extrahelp MoreHelp(
    "\nclang-vec will list all functions that accept std::vector as a"
    "\npass-by-value argument.");

int main(int argc, const char** argv) {
    llvm::sys::PrintStackTraceOnErrorSignal(argv[0], /*InstallHandler=*/true);
    clang::tooling::CommonOptionsParser Options(argc, argv, FindVecCategory);
    clang::tooling::ClangTool Tool(Options.getCompilations(),
                                   Options.getSourcePathList());

    VecCallback VC;
    clang::ast_matchers::MatchFinder Finder;
    Finder.addMatcher(M, &VC);

    return Tool.run(clang::tooling::newFrontendActionFactory(&Finder).get());
}
