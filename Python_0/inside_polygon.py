#!/usr/bin/python
import numpy

def insidePolygon(vertices, point, border_value=True):
    """
    Return True/False is a pixel is inside a polygon.

    @param vertices:
    @param point: 2-tuple of integers or array
    @param border_value: boolean
    """
  counter = 0;
  int i;
  double xinters;
  Point p1,p2;

  p1 = polygon[0];
  for (i=1;i<=N;i++) {
    if ((p1.x == p.x) && (p1.y == p.y))
        return border_value;
    p2 = polygon[i % N];
    if (p.y > MIN(p1.y,p2.y)) {
      if (p.y <= MAX(p1.y,p2.y)) {
        if (p.x <= MAX(p1.x,p2.x)) {
          if (p1.y != p2.y) {
            xinters = (p.y-p1.y)*(p2.x-p1.x)/(p2.y-p1.y)+p1.x;
            if (p1.x == p2.x || p.x <= xinters)
              counter++;
          }
        }
      }
    }
    p1 = p2;
  }

  if (counter % 2 == 0)
    return(OUTSIDE);
  else
    return(INSIDE);
}

class Polygon(object):
    def __init__(self, vertices):
        """
        @param vertices: Nx2 array of floats
        """
        self.vertices = vertices
    def isInside(point):


