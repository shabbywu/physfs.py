#include <pybind11/pybind11.h>
#include "shim.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)


namespace py = pybind11;


PYBIND11_MODULE(physfs, m) {
    register_physfs(m);
#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif

m.attr("__author__") = "shabbywu<shabbywu@qq.com>";
}