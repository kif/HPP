__kernel void vadd(__global const float *a,
				     __global const float *b,
				     __global       float *c,
				     int N)
 {
     int gid = get_global_id(0);
     if (gid<N)
    	 c[gid]  = a[gid] + b[gid];
 }