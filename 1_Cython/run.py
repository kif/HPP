#!/usr/bin/env python
#coding: utf-8

import numpy
import inside_polygon
import time
n = 24
LEN = 1024

if __name__ == "__main__":
    vertices = inside_polygon.make_vertices(n)
    print vertices

    t0 = time.time()
    res = []
    for x in range(LEN):
        res.append([inside_polygon.inside_polygon(vertices, (x, y)) for y in range(LEN)])
    print("execution time Cython: %.3fs" % (time.time() - t0))

    vertices = numpy.array(vertices).astype(numpy.float32)
#     print vertices
    poly = inside_polygon.Polygon(vertices)

    t0 = time.time()
    res = []
    for x in range(LEN):
        res.append([inside_polygon.inside_polygon_np(vertices, (x, y)) for y in range(LEN)])
    print("execution time Cython+Numpy+Opt: %.3fs" % (time.time() - t0))

    t0 = time.time()
    res = []
    for x in range(LEN):
        res.append([poly.isInside(x, y) for y in range(LEN)])
    print("execution time Cython+Numpy+class: %.3fs" % (time.time() - t0))
    t0 = time.time()
    msk = poly.make_mask(LEN, LEN)
    print("execution time Cython+Numpy+class+Opt+loop: %.3fs" % (time.time() - t0))

    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "-q":
        sys.exit()
    import pylab
    pylab.imshow(msk)
    last = vertices[-1]
    for v in vertices:
        pylab.annotate("", xy=v, xytext=last, xycoords="data",
                 arrowprops=dict(arrowstyle="-"))
        last = v
    pylab.show()
