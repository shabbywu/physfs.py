# CMakeList.txt: 顶层 CMake 项目文件，在此处执行全局配置
# 并包含子项目。
#
cmake_minimum_required (VERSION 3.15)

# Enable Hot Reload for MSVC compilers if supported.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

# Enable VCPKG if VCPKG_ROOT defined.
if (DEFINED ENV{VCPKG_ROOT})
  set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" CACHE FILEPATH "")
endif()

project ("physfs.py")

set(CMAKE_CXX_STANDARD 17)
set(PHYSFS_BUILD_STATIC ON CACHE BOOL "Build the bundled static PhysicsFS library" FORCE)
set(PHYSFS_BUILD_SHARED OFF CACHE BOOL "Disable the bundled shared PhysicsFS library" FORCE)
set(PHYSFS_BUILD_TEST OFF CACHE BOOL "Disable bundled PhysicsFS tests" FORCE)
set(PHYSFS_BUILD_DOCS OFF CACHE BOOL "Disable bundled PhysicsFS documentation" FORCE)
set(PHYSFS_DISABLE_INSTALL ON CACHE BOOL "Disable bundled PhysicsFS install rules" FORCE)

add_subdirectory(libs/physfs)
# 指定 PhysFS 编译参数
target_compile_options(physfs-static PRIVATE -fPIC)


set(PYBIND11_FINDPYTHON ON CACHE BOOL "Use CMake's modern FindPython support" FORCE)
add_subdirectory(libs/pybind11)
add_subdirectory(src)
