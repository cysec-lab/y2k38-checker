#include "ReadFsTimestampAction.h"

#include <clang/Frontend/FrontendPluginRegistry.h>

#include "clang/AST/AST.h"

static clang::FrontendPluginRegistry::Add<readfstimestamp::ReadFsTimestampAction> X(
    "read fs timestamp", "explain here.");
