add_library(timet-to-int-downcast-plugin MODULE
  TimetToIntDowncast.cpp
)
add_library(timet-to-int-downcast STATIC
  TimetToIntDowncast.cpp
)

target_include_directories(timet-to-int-downcast
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS timet-to-int-downcast DESTINATION lib)
