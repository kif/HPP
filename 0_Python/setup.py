#!/usr/bin/env python

from distutils.core import setup
from Cython.Distutils import build_ext
from distutils.extension import Extension

# Under windows, numpy include file needs to be provided.
# from numpy.distutils.core import Extension

cy_mod = Extension("inside_polygon",
                   sources=["inside_polygon.pyx"],
                   )

setup(ext_modules=[cy_mod],
	cmdclass={'build_ext': build_ext})
