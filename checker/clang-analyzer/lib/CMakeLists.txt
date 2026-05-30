function(add_y2k38_check NAME SOURCE)
  add_library(${NAME}-plugin MODULE ${SOURCE})
  add_library(${NAME} STATIC ${SOURCE})
  target_include_directories(${NAME}
    INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
  )
  install(TARGETS ${NAME} DESTINATION lib)
endfunction()

add_subdirectory(read-fs-timestamp)
add_subdirectory(write-fs-timestamp)
add_subdirectory(timet-to-int-downcast)
add_subdirectory(timet-to-long-downcast)
add_subdirectory(y2k38-all)
