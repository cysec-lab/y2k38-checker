add_library(timet-to-long-downcast-plugin MODULE
  TimetToLongDowncast.cpp
)
add_library(timet-to-long-downcast STATIC
  TimetToLongDowncast.cpp
)

target_include_directories(timet-to-long-downcast
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS timet-to-long-downcast DESTINATION lib)
