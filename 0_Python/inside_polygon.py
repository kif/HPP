#!/usr/bin/python
import numpy, random


def insidePolygon(vertices, point, border_value=True):
    """
    Return True/False is a pixel is inside a polygon.

    @param vertices:
    @param point: 2-tuple of integers or list
    @param border_value: boolean
    """
    counter = 0
    for i,polypoint1 in enumerate(vertices):
        if (polypoint1[0] == point[0]) and (polypoint1[1] == point[1]):
            return border_value
        polypoint2 = vertices[(i+1)%len(vertices)]
        if (point[1] > min(polypoint1[1], polypoint2[1])):
            if (point[1] <= max(polypoint1[1], polypoint2[1])):
                if (point[0] <= max(polypoint1[0], polypoint2[0])):
                    if (polypoint1[1] != polypoint2[1]):
                        xinters = (point[1]-polypoint1[1])*(polypoint2[0]-polypoint1[0])/(polypoint2[1]-polypoint1[1])+polypoint1[0]
                        if (polypoint1[0] == polypoint2[0]) or (point[0] <= xinters):
                            counter+=1
    if counter % 2 == 0:
        return False
    else:
        return True

def insidePolygon_np(vertices, point, border_value=True):
    """
    Return True/False is a pixel is inside a polygon.

    @param vertices: numpy ndarray Nx2
    @param point: 2-tuple of integers or list
    @param border_value: boolean

    Numpy implementation.
    """
    counter = 0
    px, py = point[0], point[1]
    nvert = vertices.shape[0]
    polypoint1x, polypoint1y = vertices[nvert - 1, 0], vertices[nvert - 1, 1]
    for i in range(nvert):
        if (polypoint1x == px) and (polypoint1y == py):
            return border_value
        polypoint2x, polypoint2y = vertices[i, 0], vertices[i, 1]
        if (py > min(polypoint1y, polypoint2y)):
            if (py <= max(polypoint1y, polypoint2y)):
                if (px <= max(polypoint1x, polypoint2x)):
                    if (polypoint1y != polypoint2y):
                        xinters = (py - polypoint1y) * (polypoint2x - polypoint1x) / (polypoint2y - polypoint1y) + polypoint1x
                        if (polypoint1x == polypoint2x) or (px <= xinters):
                            counter += 1
        polypoint1x, polypoint1y = polypoint2x, polypoint2y
    if counter % 2 == 0:
        return False
    else:
        return True


class Polygon(object):
    def __init__(self, vertices):
        """
        @param vertices: Nx2 array of floats
        """
        self.vertices = vertices
        self.nvert = vertices.shape[0]

    def isInside(self, point, border_value=True):
        """
        Return True/False is a pixel is inside a polygon.

        @param vertices: numpy ndarray Nx2
        @param point: 2-tuple of integers or list
        @param border_value: boolean

        Numpy implementation.
        """
        counter = 0
        px, py = point[0], point[1]
        n = self.vertices.shape[0]
        polypoint1x, polypoint1y = self.vertices[self.nvert - 1, 0], self.vertices[self.nvert - 1, 1]
        for i in range(self.nvert):
            if (polypoint1x == px) and (polypoint1y == py):
                return border_value
            polypoint2x, polypoint2y = self.vertices[i, 0], self.vertices[i, 1]
            if (py > min(polypoint1y, polypoint2y)):
                if (py <= max(polypoint1y, polypoint2y)):
                    if (px <= max(polypoint1x, polypoint2x)):
                        if (polypoint1y != polypoint2y):
                            xinters = (py - polypoint1y) * (polypoint2x - polypoint1x) / (polypoint2y - polypoint1y) + polypoint1x
                            if (polypoint1x == polypoint2x) or (px <= xinters):
                                counter += 1
            polypoint1x, polypoint1y = polypoint2x, polypoint2y
        if counter % 2 == 0:
            return False
        else:
            return True
            pass


def make_vertices(nr,max_val=1024):
    """
    Generates a set of vertices as nr-tuple of 2-tuple of integers
    """
    import random
    return tuple([(random.randint(0, max_val), random.randint(0, max_val)) for i in range(nr)])

def make_vertices_np(nr, max_val=1024):
    """
    Generates a set of vertices as nr-tuple of 2-tuple of integers
    """
    import numpy
    return numpy.random.randint(0, max_val, nr * 2).reshape((nr, 2)).astype(numpy.float32)

if __name__ == "__main__":
    import time
    n=24
    vertices = make_vertices(n)
    print vertices

    t0 = time.time()
    res = []
    for x in range(1024):
        res.append([insidePolygon(vertices, (x, y)) for y in range(1024)])
    print("execution time tuples: %.3fs" % (time.time() - t0))

    vertices = numpy.array(vertices,dtype=numpy.float32)
    print vertices
    t0 = time.time()
    res = []
    for x in range(1024):
        res.append([insidePolygon_np(vertices, (x, y))  for y in range(1024)])
    print("execution time numpy: %.3fs" % (time.time() - t0))
    poly = Polygon(vertices)
    t0 = time.time()
    res = []
    for x in range(1024):
        res.append([poly.isInside((x, y))  for y in range(1024)])
    print("execution time numpy: %.3fs" % (time.time() - t0))




