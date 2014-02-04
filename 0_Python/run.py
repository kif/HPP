import inside_polygon

if __name__ == "__main__":
    import time
    N = 24
    L = 1024
    vertices = inside_polygon.make_vertices(N)
    print vertices

    t0 = time.time()
    res = []
    for x in range(L):
        res.append([inside_polygon.insidePolygon(vertices, (x, y)) for y in range(L)])
    print("execution time tuples: %.3fs" % (time.time() - t0))

    import numpy
    vertices = numpy.array(vertices, dtype=numpy.float32)
    # print vertices
    t0 = time.time()
    res = []
    for x in range(L):
        res.append([inside_polygon.insidePolygon_np(vertices, (x, y))  for y in range(L)])
    print("execution time numpy: %.3fs" % (time.time() - t0))
    poly = inside_polygon.Polygon(vertices)
    t0 = time.time()
    res = []
    for x in range(L):
        res.append([poly.isInside((x, y))  for y in range(L)])
    print("execution time class+numpy: %.3fs" % (time.time() - t0))
    msk = numpy.array(res)

#    t0 = time.time()
#    msk = poly.make_mask(L, L)
#    print("execution time Cython+Numpy+class+Opt+OpenMP: %.3fs" % (time.time() - t0))
    import pylab
    pylab.imshow(msk.T)
    last = vertices[-1]
    for v in vertices:
        pylab.annotate("", xy=v, xytext=last, xycoords="data",
                 arrowprops=dict(arrowstyle="-"))
        last = v
    pylab.show()
