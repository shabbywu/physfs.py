# Available at setup time due to pyproject.toml
import platform
import os
from pathlib import Path
from glob import glob
from distutils import log

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools.command.build_clib import build_clib as _build_clib
from setuptools import setup, Extension
from setuptools.extension import Library

__version__ = "0.0.2"
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"


ext_libraries = [
   [
      "physfs", 
      {
         "sources": ["libs/physfs"],
         "type": "cmake",
         "cmake_args": [
            # disable build shared library for macos and linux
            "-DPHYSFS_BUILD_SHARED=false"
            if not IS_WINDOWS else 
            # disable build static library for windows(before something wrong in windows)
            "-DPHYSFS_BUILD_STATIC=false",
            # disable build test
            "-DPHYSFS_BUILD_TEST=false", 
            # disable build docs
            "-DPHYSFS_BUILD_DOCS=false", 
            # set -fPIC
            "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
         ],
         "copy_objects": [] if not IS_WINDOWS else ["physfs.dll"]
      }
   ]
]


extra_link_args = []
if IS_MACOS:
   extra_link_args = ["-framework", "IOKit", "-framework", "Foundation"]


ext_modules = [
    Pybind11Extension("physfs",
        ["src/main.cpp", "src/shim.cpp"],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        include_dirs=["libs/physfs/src"],
        extra_link_args=extra_link_args,
    ),
]


class build_clib(_build_clib):
   def build_libraries(self, libraries):
      cwd = Path().absolute()
      other_libraries = []
      for (lib_name, build_info) in libraries:
         if build_info.get("type") != "cmake":
            libraries.append((lib_name, build_info))
            continue

         log.info("building '%s' library", lib_name)
         src = Path(build_info["sources"][0]).absolute()
         build_temp = (Path(self.build_temp) / lib_name).absolute()
         build_temp.mkdir(parents=True, exist_ok=True)
         config = 'Debug' if self.debug else 'Release'
         build_dest = build_temp / config if IS_WINDOWS else build_temp

         build_ext = self.get_finalized_command('build_ext')
         build_lib = Path(build_ext.build_lib).absolute()
         cmake_args = [
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + str(build_temp),
            '-DCMAKE_BUILD_TYPE=' + config,
            *build_info.get("cmake_args", [])
         ]
         build_args = [
            '--config', config,
            "-v"
         ]
         os.chdir(str(build_temp))
         self.spawn(['cmake', str(src)] + cmake_args)
         if not self.dry_run:
            self.spawn(['cmake', '--build', '.'] + build_args)
            # extend library_dirs
            for ext in build_ext.extensions:
               ext.library_dirs.append(str(build_dest))
            # copy objects to dest
            build_lib.mkdir(parents=True, exist_ok=True)
            copy_objects = build_info.get("copy_objects")
            if copy_objects:
               for obj in copy_objects:
                  self.copy_file(str(build_dest / obj), str(build_lib / obj))
         os.chdir(str(cwd))
      return super().build_libraries(other_libraries)


setup(
    name="physfs.py",
    version=__version__,
    author="shabbywu",
    author_email="shabbywu@qq.com",
    url="https://github.com/shabbywu/physfs.py",
    description="PhysFS.py is a python wrapper for the PhysicsFS library.",
    long_description="",
    ext_modules=ext_modules,
    libraries=ext_libraries,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext, "build_clib": build_clib},
    zip_safe=False,
    python_requires=">=3.7",
)
