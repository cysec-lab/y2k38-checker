#include "TimetToLongDowncast.h"

#include <clang/Frontend/FrontendPluginRegistry.h>

#include "clang/AST/AST.h"

static clang::FrontendPluginRegistry::Add<
    timet_to_long_downcast::TimetToLongDowncastAction>
    X("time_t to long downcast", "explain here.");
