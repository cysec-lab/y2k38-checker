add_library(stat-checker-plugin MODULE
  CheckStatAction.cpp
)
add_library(stat-checker STATIC
  CheckStatAction.cpp
)

target_include_directories(stat-checker
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS stat-checker DESTINATION lib)

