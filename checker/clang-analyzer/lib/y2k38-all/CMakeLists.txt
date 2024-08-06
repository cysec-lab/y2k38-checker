add_library(y2k38-plugin MODULE
  Y2k38AllAction.cpp
)
add_library(y2k38-all STATIC
  Y2k38AllAction.cpp
)

target_include_directories(y2k38-all
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS y2k38-all DESTINATION lib)
