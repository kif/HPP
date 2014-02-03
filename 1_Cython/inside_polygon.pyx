#!/usr/bin/python



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

    @param vertices:
    @param point: 2-tuple of integers or list
    @param border_value: boolean
    
    Numpy implementation.
    """
    vx, vy = vertices[:, 0], vertices[:, 1]
    x, y = point
    c = 0
    j = len(vertices) - 1
    for i in xrange(len(vertices)):
        if(((vy[i] > y) != (vy[j] > y)) and (x < (vx[j] - vx[i]) *
                                              (y - vy[i]) / (vy[j] - vy[i]) + vx[i])):
            c = 1 - c
        j = i
    return c

class Polygon(object):
    def __init__(self, vertices):
        """
        @param vertices: Nx2 array of floats
        """
        self.vertices = vertices
    def isInside(point):
        pass


def make_vertices(nr,max_val=1024):
    """
    Generates a set of vertices as nr-tuple of 2-tuple if integers
    """
    import random
    return tuple([(random.randint(0, max_val), random.randint(0, max_val)) for i in range(nr)])

def make_vertices_np(nr, max_val=1024):
    """
    Generates a set of vertices as nr-tuple of 2-tuple if integers
    """
    import numpy
    return numpy.random.randint(0, max_val, nr * 2).reshape((nr, 2))

if __name__ == "__main__":
    import time
    n=24
    vertices = make_vertices(n)
    print vertices

    t0 = time.time()
    res = []
    for x in range(1024):
        line = []
        for y in range(1024):
            line.append(insidePolygon(vertices, (x, y)))
        res.append(line)
    print("execution time: %.3fs" % (time.time() - t0))
#    print res



    
