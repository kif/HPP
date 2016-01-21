#!/usr/bin/env python
# coding: utf-8
from __future__ import division

__doc__ = """
demo of inside_polygon
"""
__author__ = "Jérôme Kieffer"
__copyright__ = "2014-16 ESRF"
__contact__ = "Jerome.Kieffer@esrf.fr"
__license__ = "MIT"

import inside_polygon
import numpy
import time

display = False

if __name__ == "__main__":
    N = 24
    L = 1024
    vertices = inside_polygon.make_vertices(N)
    print vertices

    t0 = time.time()
    res = []
    for x in range(L):
        res.append([inside_polygon.in_polygon(vertices, (x, y)) for y in range(L)])
    print("execution time tuples: %.3fs" % (time.time() - t0))

    vertices = numpy.array(vertices, dtype=numpy.float32)
    # print vertices
    t0 = time.time()
    res = []
    for x in range(L):
        res.append([inside_polygon.in_polygon_np(vertices, (x, y))  for y in range(L)])
    print("execution time numpy: %.3fs" % (time.time() - t0))
    poly = inside_polygon.Polygon(vertices)
    t0 = time.time()
    res = []
    for x in range(L):
        res.append([poly.is_inside((x, y))  for y in range(L)])
    print("execution time class+numpy: %.3fs" % (time.time() - t0))
    msk = numpy.array(res)

#    t0 = time.time()
#    msk = poly.make_mask(L, L)
#    print("execution time Cython+Numpy+class+Opt+OpenMP: %.3fs" % (time.time() - t0))
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "-q":
        sys.exit()
    import pylab
    pylab.imshow(msk.T)
    last = vertices[-1]
    for v in vertices:
        pylab.annotate("", xy=v, xytext=last, xycoords="data",
                 arrowprops=dict(arrowstyle="-"))
        last = v
    pylab.show()
