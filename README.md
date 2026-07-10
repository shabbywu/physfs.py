PhysFS.py
==============

![github-stars][stars-badge]

| CI | status |
|----|--------|
| Source install | [![CI status][actions-ci-badge]][actions-ci-link] |
| [`cibuildwheel`][] release | [![Release status][actions-release-badge]][actions-release-link] |

[stars-badge]:             https://img.shields.io/github/stars/shabbywu/physfs.py?style=social
[actions-ci-link]:         https://github.com/shabbywu/physfs.py/actions/workflows/ci.yml
[actions-ci-badge]:        https://github.com/shabbywu/physfs.py/actions/workflows/ci.yml/badge.svg?branch=master
[actions-release-link]:    https://github.com/shabbywu/physfs.py/actions/workflows/release.yml
[actions-release-badge]:   https://github.com/shabbywu/physfs.py/actions/workflows/release.yml/badge.svg
[`cibuildwheel`]:          https://cibuildwheel.pypa.io

PhysFS.py is a python wrapper for the PhysicsFS library.

Installation
------------

- `pip install physfs.py`

Requirements
------------

- CPython 3.8 or newer.
- CMake 3.15 or newer, pybind11 2.10 or newer, and a C++17 compiler when
  building from source. pip installs the build dependencies automatically.
- Prebuilt macOS wheels target Apple Silicon (`arm64`) only; Intel macOS uses the source distribution.

Features
------------
physfs.py provides an encapsulation of the basic interface of PhysFS, including `init`, `deinit`, `mount`, `mount_memory`, `unmount`, `ls`, `read(cat)`, `stat`.

Enables python to use PhysFS at a minimum.

License
-------

pybind11 is provided under a BSD-style license that can be found in the LICENSE
file. By using, distributing, or contributing to this project, you agree to the
terms and conditions of this license.

Test call
---------

```python
import physfs
physfs.init()

physfs.mount("./example.zip")
physfs.ls()
```
