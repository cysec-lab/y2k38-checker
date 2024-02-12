add_library(write-fs-timestamp-plugin MODULE
  WriteFsTimestampAction.cpp
)
add_library(write-fs-timestamp STATIC
  WriteFsTimestampAction.cpp
)

target_include_directories(write-fs-timestamp
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS write-fs-timestamp DESTINATION lib)
