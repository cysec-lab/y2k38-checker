add_library(explicit-downcast-plugin MODULE
  ExplicitDowncast.cpp
)
add_library(explicit-downcast STATIC
ExplicitDowncast.cpp
)

target_include_directories(explicit-downcast
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS explicit-downcast DESTINATION lib)
