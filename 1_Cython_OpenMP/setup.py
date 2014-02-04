#!/usr/bin/python
from distutils.core import setup
from Cython.Distutils import build_ext
from distutils.extension import Extension
cy_mod = Extension("inside_polygon",
    sources=["inside_polygon.pyx"],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'],
    language="c")
setup(ext_modules=[cy_mod],
    cmdclass={'build_ext': build_ext})
