cdef extern from "InsidePolygonWithBounds.h":
    void PointsInsidePolygon(double *, int , \
                             double *, int , int , unsigned char *)

# void PointsInsidePolygon(double *polygon_xy, int N_xy, \
#                          double *points_xy, int N_points_xy,
#                          int border_value, unsigned char *output);
