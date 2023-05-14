#include "Y2k38CheckerAction.h"

#include <clang/Frontend/FrontendPluginRegistry.h>

#include "clang/AST/AST.h"

static clang::FrontendPluginRegistry::Add<y2k38checker::Y2k38CheckerAction> X(
    "y2k38-checker", "explain here.");