#!/usr/bin/python

import numpy
import pyopencl

LENGTH = 1024
# create context, queue and program
ctx = pyopencl.create_some_context()
queue = pyopencl.CommandQueue(context)
src = open('vadd.cl').read()
prg = pyopencl.Program(ctx, kernelsource).build()

# create host arrays
h_a = numpy.random.rand(N).astype(numpy.float32)
h_b = numpy.random.rand(N).astype(numpy.float32)
h_c = numpy.empty(N, dtype=numpy.float32)

# create device buffers
mf = pyopencl.mem_flags
d_a = pyopencl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=h_a)
d_b = pyopencl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=h_b)
d_c = pyopencl.Buffer(ctx, mf.WRITE_ONLY, h_c.nbytes)

# run kernel
vadd = program.vadd
vadd.set_scalar_arg_dtypes([None, None, None, numpy.uint32])
vadd(queue, h_a.shape, None, d_a, d_b, d_c, N)

# return results
pyopencl.enqueue_copy(queue, h_c, d_c)
print numpy.allclose(h_a + h_b, h_c)
