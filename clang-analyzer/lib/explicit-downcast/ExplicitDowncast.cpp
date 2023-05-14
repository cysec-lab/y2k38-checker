#include "ExplicitDowncast.h"

#include <clang/Frontend/FrontendPluginRegistry.h>

#include "clang/AST/AST.h"

static clang::FrontendPluginRegistry::Add<
    explicitdowncast::ExplicitDowncastAction>
    X("explicit downcast", "explain here.");
