file(GLOB MAIN_SOURCE *.cpp *.h)

# pybind11_add_module(_squirrel NO_EXTRAS ${MAIN_SOURCE})
pybind11_add_module(physfs ${MAIN_SOURCE})
set_property(TARGET physfs PROPERTY CXX_STANDARD 17)
if(VERSION_INFO)
  target_compile_definitions(physfs PRIVATE VERSION_INFO=${VERSION_INFO})
endif()
target_include_directories(physfs PUBLIC 
  ${CMAKE_CURRENT_SOURCE_DIR}/../libs/pybind11/include
  ${CMAKE_CURRENT_SOURCE_DIR}/../libs/physfs/src
  )
target_link_libraries(physfs PUBLIC physfs-static)