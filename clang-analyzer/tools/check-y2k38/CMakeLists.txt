
add_executable(check-y2k38
  main.cpp
)

if (LLVM_ENABLE_ASSERTIONS)
  add_definitions(-DLLVM_ENABLE_ASSERTIONS=${LLVM_ENABLE_ASSERTIONS})
endif()

llvm_map_components_to_libnames(REQ_LLVM_LIBRARIES ${LLVM_TARGETS_TO_BUILD}
                                core support option
)

target_link_libraries(check-y2k38
  y2k38-checker
  read-fs-timestamp
  write-fs-timestamp
  clangAST
  clangASTMatchers
  clangBasic
  clangCodeGen
  clangLex
  clangParse
  clangSema
  clangAnalysis
  clangDriver
  clangFrontend
  clangAST
  clangEdit
  clangSerialization
  clangTooling
  clangToolingCore
  clangAST
  clangParse
  clangBasic
  clangSema
  clangAST
  ${REQ_LLVM_LIBRARIES}
)

target_include_directories(check-y2k38
  PRIVATE $<TARGET_PROPERTY:y2k38-checker,INTERFACE_INCLUDE_DIRECTORIES>
)

# Platform dependencies.
if( WIN32 )
  find_library(SHLWAPI_LIBRARY shlwapi)
  target_link_libraries(check-y2k38
    ${SHLWAPI_LIBRARY}
  )
else()
  find_package(Threads REQUIRED)
  find_package(Curses REQUIRED)
  target_link_libraries(check-y2k38
    ${CMAKE_THREAD_LIBS_INIT}
    ${CMAKE_DL_LIBS}
    ${CURSES_LIBRARIES}
  )
endif()

set_target_properties(check-y2k38
                      PROPERTIES
                      LINKER_LANGUAGE CXX
                      PREFIX ""
)

install(TARGETS check-y2k38
  RUNTIME DESTINATION bin
)
