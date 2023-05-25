PhysFS.py
==============

![github-stars][stars-badge]

|      CI              | status |
|----------------------|--------|
| Linux/macOS Travis   | [![Travis-CI][travis-badge]][travis-link] |
| MSVC 2019            | [![AppVeyor][appveyor-badge]][appveyor-link] |
| pip builds           | [![Pip Actions Status][actions-pip-badge]][actions-pip-link] |
| [`cibuildwheel`][]   | [![Wheels Actions Status][actions-wheels-badge]][actions-wheels-link] |

[gitter-badge]:            https://badges.gitter.im/pybind/Lobby.svg
[stars-badge]:             https://img.shields.io/github/stars/shabbywu/physfs.py?style=social
[actions-badge]:           https://github.com/shabbywu/physfs.py/workflows/Tests/badge.svg
[actions-pip-link]:        https://github.com/shabbywu/physfs.py/actions?query=workflow%3A%22Pip
[actions-pip-badge]:       https://github.com/shabbywu/physfs.py/workflows/Pip/badge.svg
[actions-wheels-link]:     https://github.com/shabbywu/physfs.py/actions?query=workflow%3AWheels
[actions-wheels-badge]:    https://github.com/shabbywu/physfs.py/workflows/Wheels/badge.svg
[travis-link]:             https://travis-ci.org/shabbywu/physfs.py
[travis-badge]:            https://travis-ci.org/shabbywu/physfs.py.svg?branch=master&status=passed
[appveyor-link]:           https://ci.appveyor.com/project/shabbywu/physfs.py
<!-- TODO: get a real badge link for appveyor -->
[appveyor-badge]:          https://travis-ci.org/shabbywu/physfs.py.svg?branch=master&status=passed
[`cibuildwheel`]:          https://cibuildwheel.readthedocs.io

PhysFS.py is a python wrapper for the PhysicsFS library.

Installation
------------

 - clone this repository
 - `pip install ./physfs.py`

Requirements
------------
CMake for building, and, of course, the PhysicsFS library.

Features
------------
physfs.py provides an encapsulation of the basic interface of PhysFS, including `init`, `deinit`, `mount`, `unmount`, `ls`, `read(cat)`, `stat`.

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
