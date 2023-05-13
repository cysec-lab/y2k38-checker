#include "Y2k38CheckerAction.h"

#include <clang/Frontend/FrontendPluginRegistry.h>

#include "clang/AST/AST.h"

using namespace y2k38checker;

static clang::FrontendPluginRegistry::Add<Y2k38CheckerAction> X(
    "y2k38-checker", "explain here.");