add_library(y2k38-checker-plugin MODULE
  Y2k38CheckerAction.cpp
)
add_library(y2k38-checker STATIC
  Y2k38CheckerAction.cpp
)

target_include_directories(y2k38-checker
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS y2k38-checker DESTINATION lib)
