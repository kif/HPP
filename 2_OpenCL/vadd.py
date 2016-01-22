#!/usr/bin/env python
#coding: utf-8

import numpy
import pyopencl

L = 1024

# create context, queue and program
ctx = pyopencl.create_some_context()
queue = pyopencl.CommandQueue(ctx)
src = open('vadd.cl').read()
prg = pyopencl.Program(ctx, src).build()

# create host arrays
h_a = numpy.random.rand(L).astype(numpy.float32)
h_b = numpy.random.rand(L).astype(numpy.float32)
h_c = numpy.empty(L, dtype=numpy.float32)

# create device buffers
mf = pyopencl.mem_flags
d_a = pyopencl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=h_a)
d_b = pyopencl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=h_b)
d_c = pyopencl.Buffer(ctx, mf.WRITE_ONLY, h_c.nbytes)

# run kernel
prg.vadd(queue, h_a.shape, (8,) , d_a, d_b, d_c, numpy.int32(L))

# return results
pyopencl.enqueue_copy(queue, h_c, d_c)
print(numpy.allclose(h_a + h_b, h_c))
