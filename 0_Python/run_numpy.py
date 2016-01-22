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

N = 24
L = 1024

if __name__ == "__main__":
    vertices = inside_polygon.make_vertices(N)
    print vertices
    vertices = numpy.array(vertices, dtype=numpy.float32)
    # print vertices
    t0 = time.time()
    res = []
    for x in range(L):
        res.append([inside_polygon.in_polygon_np(vertices, (x, y))  for y in range(L)])
    print("execution time numpy: %.3fs" % (time.time() - t0))

    msk = numpy.array(res)

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
