#include "TimetToIntDowncast.h"

#include <clang/Frontend/FrontendPluginRegistry.h>

#include "clang/AST/AST.h"

static clang::FrontendPluginRegistry::Add<
    timet_to_int_downcast::TimetToIntDowncastAction>
    X("time_t to int downcast", "explain here.");
