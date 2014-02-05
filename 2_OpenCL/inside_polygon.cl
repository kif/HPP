__kernel void 
insidePolygon(__global const float *polygon, int N,
              unsigned char border_value,
              __global unsigned char *result)
{
  int counter = 0;
  int i;
  float xinters;
  float px, py, p1x, p2x, p1y, p2y;
  unsigned char value;

  int posx = get_global_id(0);
  int posy = get_global_id(1);
  int width = get_global_size(0);
  px = (float) posx;
  py = (float) posy;
  p1x = polygon[0];
  p1y = polygon[1];
  for (i=1;i<=N;i++) {
    if ((p1x == px) && (p1y == py))
        {result[posy*width+posx]  = border_value;
         return;
	}

    p2x = polygon[2*i % (2*N)];
    p2y = polygon[2*i % (2*N)+1];
    if (py > min(p1y,p2y)) {
      if (py <= max(p1y,p2y)) {
        if (px <= max(p1x,p2x)) {
          if (p1y != p2y) {
            xinters = (py-p1y)*(p2x-p1x)/(p2y-p1y)+p1x;
            if (p1x == p2x || px <= xinters)
              counter++;
          }
        }
      }
    }
    p1x = p2x;
    p1y = p2y;
  }

  if (counter % 2 == 0)
    result[posy*width+posx] = 0;
  else
    result[posy*width+posx] = 1;
  
}
