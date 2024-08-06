#include "Y2k38AllAction.h"

#include <clang/Frontend/FrontendPluginRegistry.h>

#include "clang/AST/AST.h"

static clang::FrontendPluginRegistry::Add<
    y2k38all::Y2k38AllAction>
    X("y2k38 all", "explain here.");
