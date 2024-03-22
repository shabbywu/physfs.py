# CMakeList.txt: 顶层 CMake 项目文件，在此处执行全局配置
# 并包含子项目。
#
cmake_minimum_required (VERSION 3.8)

# Enable Hot Reload for MSVC compilers if supported.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

project ("squirrel-lang-pybinding")
set(CMAKE_CXX_STANDARD 17)
# add_compile_options(-O2 -fno-strict-aliasing)

set(PHYSFS_BUILD_STATIC "ON")
set(PHYSFS_BUILD_SHARED "OFF")
set(PHYSFS_BUILD_TEST "FALSE")
set(PHYSFS_BUILD_DOCS "FALSE")

add_subdirectory(libs/physfs)
add_subdirectory(libs/pybind11)
add_subdirectory(src)
