#!/usr/bin/python

cimport cython
import numpy
cimport numpy

from cython.parallel import prange

def inside_polygon(vertices, point, border_value=True):
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

def inside_polygon_np(vertices, point, border_value=True):
    """
    Return True/False is a pixel is inside a polygon.

    @param vertices: numpy ndarray Nx2
    @param point: 2-tuple of integers or list
    @param border_value: boolean

    Numpy implementation + Cython optimization
    """
    cdef int counter, i, nvert
    cdef float px, py, polypoint1x, polypoint1y, polypoint2x, polypoint2y, xinters
    cdef float[:,:] c_vertices =  numpy.ascontiguousarray(vertices, dtype=numpy.float32)
    counter = 0
    px, py = point[0], point[1]
    nvert = vertices.shape[0]
    polypoint1x, polypoint1y = c_vertices[nvert-1, 0],c_vertices[nvert-1, 1]
    for i in range(nvert):
        if (polypoint1x == px) and (polypoint1y == py):
            return border_value
        polypoint2x, polypoint2y = c_vertices[i, 0],c_vertices[i, 1]
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

cdef class Polygon(object):
    cdef float[:,:] vertices
    cdef int nvert
    
    def __init__(self, vertices):
        """
        @param vertices: Nx2 array of floats
        """
        self.vertices = numpy.ascontiguousarray(vertices, dtype=numpy.float32)
        self.nvert = vertices.shape[0]

    @cython.cdivision(True)
    @cython.wraparound(False)
    @cython.boundscheck(False)
    cdef bint _isInside(self, float px, float py, bint border_value) nogil:
        """
        Pure C_Cython class implementation
        """
        cdef int counter, i
        cdef float polypoint1x, polypoint1y, polypoint2x, polypoint2y, xinters
        counter = 0

        polypoint1x, polypoint1y = self.vertices[self.nvert-1, 0],self.vertices[self.nvert-1, 1]
        for i in range(self.nvert):
            if (polypoint1x == px) and (polypoint1y == py):
                return border_value
            polypoint2x, polypoint2y = self.vertices[i, 0],self.vertices[i, 1]
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
        
    def isInside(self, float px, float py, bint border_value=True):
        return self._isInside(px, py, border_value)
    
    @cython.wraparound(False)
    @cython.boundscheck(False)
    def make_mask(self, int dx, int dy):
        cdef numpy.ndarray[dtype=numpy.uint8_t,ndim=2] mask = numpy.zeros((dx,dy),dtype=numpy.uint8)
        cdef int i, j
        for i in prange(dx, nogil=True):
            for j in range(dy):
                mask[i,j] += self._isInside(j,i, True)
        return mask


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
    return numpy.random.randint(0, max_val, nr * 2).reshape((nr, 2)).astype(numpy.float32)

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
            line.append(inside_polygon(vertices, (x, y)))
        res.append(line)
    print("execution time: %.3fs" % (time.time() - t0))
#    print res




