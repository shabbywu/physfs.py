file(GLOB MAIN_SOURCE *.cpp *.h)

# pybind11_add_module(_squirrel NO_EXTRAS ${MAIN_SOURCE})
pybind11_add_module(physfs_py ${MAIN_SOURCE})
set_property(TARGET physfs_py PROPERTY CXX_STANDARD 17)
if(VERSION_INFO)
  target_compile_definitions(physfs_py PRIVATE VERSION_INFO=${VERSION_INFO})
endif()

target_include_directories(physfs_py PUBLIC 
  ${CMAKE_CURRENT_SOURCE_DIR}/../libs/pybind11/include
  ${CMAKE_CURRENT_SOURCE_DIR}/../libs/physfs/src
  )
target_link_libraries(physfs_py PUBLIC physfs-static)


set_target_properties(physfs_py PROPERTIES OUTPUT_NAME "physfs")