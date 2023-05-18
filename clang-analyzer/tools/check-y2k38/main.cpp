
#include <unistd.h>

#include <memory>
#include <string>

#include "ReadFsTimestampAction.h"
#include "TimetToIntDowncast.h"
#include "TimetToLongDowncast.h"
#include "WriteFsTimestampAction.h"
#include "clang/Tooling/CompilationDatabase.h"
#include "llvm/Support/CommandLine.h"
#include "llvm/Support/PrettyStackTrace.h"
#include "llvm/Support/Signals.h"
#include "llvm/Support/raw_ostream.h"

using namespace llvm;

static cl::OptionCategory Category{"my-options"};

static cl::opt<std::string> databasePath{
    "p", cl::desc{"Path to compilation database"}, cl::Optional,
    cl::cat{Category}};

static cl::opt<std::string> directCompiler{cl::Positional,
                                           cl::desc{"[-- <compiler>"},
                                           cl::cat{Category}, cl::init("")};

static cl::list<std::string> directArgv{
    cl::ConsumeAfter, cl::desc{"<compiler arguments>...]"}, cl::cat{Category}};

class CommandLineCompilationDatabase
    : public clang::tooling::CompilationDatabase {
   private:
    clang::tooling::CompileCommand compileCommand;
    std::string sourceFile;

   public:
    CommandLineCompilationDatabase(llvm::StringRef sourceFile,
                                   std::vector<std::string> commandLine)
        : compileCommand(".", sourceFile, std::move(commandLine), "dummy.o"),
          sourceFile{sourceFile} {}

    std::vector<clang::tooling::CompileCommand> getCompileCommands(
        llvm::StringRef filePath) const override {
        if (filePath == sourceFile) {
            return {compileCommand};
        }
        return {};
    }

    std::vector<std::string> getAllFiles() const override {
        return {sourceFile};
    }

    std::vector<clang::tooling::CompileCommand> getAllCompileCommands()
        const override {
        return {compileCommand};
    }
};

std::unique_ptr<clang::tooling::CompilationDatabase> createDBFromCommandLine(
    llvm::StringRef compiler, llvm::ArrayRef<std::string> commandLine,
    std::string &errors) {
    auto source = std::find(commandLine.begin(), commandLine.end(), "-c");
    if (source == commandLine.end() || ++source == commandLine.end()) {
        errors = "Command line must contain '-c <source file>'";
        return {};
    }
    llvm::SmallString<128> absolutePath(*source);
    llvm::sys::fs::make_absolute(absolutePath);

    std::vector<std::string> args;
    if (compiler.endswith("++")) {
        args.push_back("c++");
    } else {
        args.push_back("cc");
    }

    args.insert(args.end(), commandLine.begin(), commandLine.end());
    return std::make_unique<CommandLineCompilationDatabase>(absolutePath,
                                                            std::move(args));
}

static std::unique_ptr<clang::tooling::CompilationDatabase>
getCompilationDatabase(std::string &errors) {
    using Database = clang::tooling::CompilationDatabase;
    if (!directCompiler.empty()) {
        return createDBFromCommandLine(directCompiler, directArgv, errors);
    } else if (!databasePath.empty()) {
        return Database::autoDetectFromDirectory(databasePath, errors);
    } else {
        char buffer[256];
        if (!getcwd(buffer, 256)) {
            llvm::report_fatal_error(
                "Unable to get current working directory.");
        }
        return Database::autoDetectFromDirectory(buffer, errors);
    }
}

static void processDatabase(
    clang::tooling::CompilationDatabase const &database) {
    auto sourcePaths = database.getAllFiles();
    clang::tooling::ClangTool tool{database, sourcePaths};
    tool.appendArgumentsAdjuster(clang::tooling::getClangStripOutputAdjuster());

    auto ReadFsTSfrontendFactory = clang::tooling::newFrontendActionFactory<
        readfstimestamp::ReadFsTimestampAction>();
    tool.run(ReadFsTSfrontendFactory.get());

    auto WriteFsTSfrontendFactory = clang::tooling::newFrontendActionFactory<
        writefstimestamp::WriteFsTimestampAction>();
    tool.run(WriteFsTSfrontendFactory.get());

    auto TimetToIntFrontendFactory = clang::tooling::newFrontendActionFactory<
        timet_to_int_downcast::TimetToIntDowncastAction>();
    tool.run(TimetToIntFrontendFactory.get());

    auto TimetToLongFrontendFactory = clang::tooling::newFrontendActionFactory<
        timet_to_long_downcast::TimetToLongDowncastAction>();
    tool.run(TimetToLongFrontendFactory.get());
}

// void warnAboutDebugBuild(llvm::StringRef programName) {
//     const unsigned COLUMNS = 80;
//     const char SEPARATOR = '*';

//     llvm::outs().changeColor(llvm::raw_ostream::Colors::YELLOW, true);
//     for (unsigned i = 0; i < COLUMNS; ++i) {
//         llvm::outs().write(SEPARATOR);
//     }

//     llvm::outs().changeColor(llvm::raw_ostream::Colors::RED, true);
//     llvm::outs() << "\nWARNING: ";
//     llvm::outs().resetColor();
//     llvm::outs() << programName
//                  << " appears to have been built in debug mode.\n"
//                  << "Your analysis may take longer than normal.\n";

//     llvm::outs().changeColor(llvm::raw_ostream::Colors::YELLOW, true);
//     for (unsigned i = 0; i < COLUMNS; ++i) {
//         llvm::outs().write(SEPARATOR);
//     }
//     llvm::outs().resetColor();
//     llvm::outs() << "\n\n";
// }

int main(int argc, char const **argv) {
    sys::PrintStackTraceOnErrorSignal(argv[0]);
    llvm::PrettyStackTraceProgram X(argc, argv);
    llvm_shutdown_obj shutdown;

    cl::HideUnrelatedOptions(Category);
    cl::ParseCommandLineOptions(argc, argv);

    // #if !defined(NDEBUG) || defined(LLVM_ENABLE_ASSERTIONS)
    //     warnAboutDebugBuild(argv[0]);
    // #endif

    std::string error;
    auto compilationDB = getCompilationDatabase(error);
    if (!compilationDB) {
        llvm::errs() << "Error while trying to load a compilation database:\n"
                     << error << "\n";
        return -1;
    }

    processDatabase(*compilationDB);

    return 0;
}
