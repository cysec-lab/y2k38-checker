add_library(read-fs-timestamp-plugin MODULE
  ReadFsTimestampAction.cpp
)
add_library(read-fs-timestamp STATIC
  ReadFsTimestampAction.cpp
)

target_include_directories(read-fs-timestamp
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS read-fs-timestamp DESTINATION lib)
