#include "WriteFsTimestampAction.h"

#include <clang/Frontend/FrontendPluginRegistry.h>

#include "clang/AST/AST.h"

static clang::FrontendPluginRegistry::Add<writefstimestamp::WriteFsTimestampAction> X(
    "write fs timestamp", "explain here.");
