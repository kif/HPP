import inside_polygon
if __name__ == "__main__":
    import time
    n = 24
    vertices = inside_polygon.make_vertices(n)
    print vertices

    t0 = time.time()
    res = []
    for x in range(1024):
        line = []
        for y in range(1024):
            line.append(inside_polygon.insidePolygon(vertices, (x, y)))
        res.append(line)
    print("execution time: %.3fs" % (time.time() - t0))
#    print res
