#!/usr/bin/env python
# coding: utf-8

import inside_polygon
import time

n = 24
L = 1024

if __name__ == "__main__":

    vertices = inside_polygon.make_vertices_np(n, L)
    print vertices

#     poly = inside_polygon.Polygon(vertices)
#     t0 = time.time()
#     msk = poly.make_mask(L, L)
#     print("execution time Cython+classes: %.3fs" % (time.time() - t0))


    t0 = time.time()
    msk = inside_polygon.make_mask(vertices, (L, L))
    print("execution time Cython+C: %.3fs" % (time.time() - t0))
#     print(msk)
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
