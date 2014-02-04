import inside_polygon
if __name__ == "__main__":
    import time
    n = 24
    LEN = 1024
    vertices = inside_polygon.make_vertices_np(n)
    print vertices
    poly = inside_polygon.Polygon(vertices)

    t0 = time.time()
    res = []
    for x in range(LEN):
        res.append([inside_polygon.insidePolygon_np(vertices, (x, y)) for y in range(LEN)])
    print("execution time Cython+Numpy+Opt: %.3fs" % (time.time() - t0))

    t0 = time.time()
    res = []
    for x in range(LEN):
        line = [poly.isInside(x, y) for y in range(LEN)]
#        for y in range(1024):
#            line.append(inside_polygon.insidePolygon_np(vertices, (x, y)))
        res.append(line)
    print("execution time Cython+Numpy+class+Opt: %.3fs" % (time.time() - t0))
    t0 = time.time()
    poly.make_mask(LEN, LEN)
    print("execution time Cython+Numpy+class+Opt+OpenMP: %.3fs" % (time.time() - t0))
