#!/usr/bin/env python
#coding:utf-8

import sys
import time
import inside_polygon
N = 24
L = 1024

if __name__ == "__main__":
    vertices = inside_polygon.make_vertices_np(N)
    print vertices
    poly = inside_polygon.Polygon(vertices)

    t0 = time.time()
    msk = poly.make_mask(L, L)
    print("execution time Cython+Numpy+class+Opt+OpenMP: %.3fs" % (time.time() - t0))

    if len(sys.argv) == 2 and sys.argv[1] == "-q":
        sys.exit()

    import pylab
    print msk
    pylab.imshow(msk)
    last = vertices[-1]
    for v in vertices:
        pylab.annotate("", xy=v, xytext=last, xycoords="data",
                 arrowprops=dict(arrowstyle="-"))
        last = v
    pylab.show()
