# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:11:54 2019

@author: sreynolds
"""

# built-in modules
import sys, os, ctypes
# common modules
import numpy

# custom modules
#  load the C-library
if sys.platform.lower() in ["linux", "linux2"]:
    shared_lib_path = os.path.abspath(os.path.join(__file__, '..', 'libpycpp.so'))
elif sys.platform.lower() == "darwin":
    shared_lib_path = os.path.abspath(os.path.join(__file__, '..', 'libpycpp.dylib'))
elif sys.platform.lower() in ["win32", "linux2"]:
    shared_lib_path = os.path.abspath(os.path.join(__file__, '..', 'pycpp.dll'))
else:
    raise RuntimeError("I cannot figure out which OS you're using")

CPYCPPLIB = ctypes.cdll.LoadLibrary(shared_lib_path)

def adder_py(a,b):
    # for fairness in timing, I'm going to do all the same checks as the C
    # version. In reality, you wouldn't be doing this. The hope for the speed-up
    # is that by vectorizing a call that cannot be done in Python without a
    # for-loop, you'll get your speed up. Here, you'll loose speed due to extra
    # checks that Python handles.

    # check correct object
    if ((not isinstance(a, numpy.ndarray)) or (not isinstance(b, numpy.ndarray))):
        raise RuntimeError("input must be numpy.ndarray type")

    if (a.size != b.size):
        raise RuntimeError("inputs not the same size")

    # check data types implemented in C
    dtypes = [numpy.float32, numpy.float64]
    if ((a.dtype not in dtypes) or (b.dtype not in dtypes)):
        raise RuntimeError("Only implemented float (32) and double (64)")

    # promote (or fail if not the same, I'm going to promote)
    if (a.dtype != b.dtype):
        if a.dtype == numpy.float64:
            b = b.astype(numpy.float64)
        if b.dtype == numpy.float64:
            a = a.astype(numpy.float64)

    return (a+b)

def adder(a, b):
    """
    adds two numpy.ndarray types returning (a+b) element-wise.
    """
    # check correct object
    if ((not isinstance(a, numpy.ndarray)) or (not isinstance(b, numpy.ndarray))):
        raise RuntimeError("input must be numpy.ndarray type")

    if (a.size != b.size):
        raise RuntimeError("inputs not the same size")

    # check data types implemented in C
    dtypes = [numpy.float32, numpy.float64]
    if ((a.dtype not in dtypes) or (b.dtype not in dtypes)):
        raise RuntimeError("Only implemented float (32) and double (64)")

    # promote (or fail if not the same, I'm going to promote)
    if (a.dtype != b.dtype):
        if a.dtype == numpy.float64:
            b = b.astype(numpy.float64)
        if b.dtype == numpy.float64:
            a = a.astype(numpy.float64)

    # get pointers to data we need
    out = numpy.zeros_like(a)
    ap = numpy.ctypeslib.as_ctypes(a)
    bp = numpy.ctypeslib.as_ctypes(b)
    outp = numpy.ctypeslib.as_ctypes(out)
    size = (ctypes.c_uint64)(a.size)

    # call it, operation now in place
    if a.dtype == numpy.float64:
        CPYCPPLIB.adder_d(ap, bp, outp, size)
    elif a.dtype == numpy.float32:
        CPYCPPLIB.adder_f(ap, bp, outp, size)
    # add more here if you want more data types supported

    # recall, it was in place so the numpy array is already updated
    return out

if __name__ == "__main__":
    import datetime
    a = numpy.arange(100, dtype=numpy.float32)
    b = a.copy()
    t1 = datetime.datetime.now()
    for n in range(1000):
        out = adder_py(a, b)
    t1 = (datetime.datetime.now() - t1).total_seconds()
    t2 = datetime.datetime.now()
    for n in range(1000):
        cout = adder(a,b)
    t2 = (datetime.datetime.now() - t2).total_seconds()

    import matplotlib.pyplot as plt
    print('Done: ' + str(cout[15]))
# =============================================================================
#     plt.figure()
#     plt.title("Compare NumPy to C")
#     plt.plot(out, 'k')
#     plt.plot(cout, '--r')
#     plt.legend(["NumPy: %0.3es"%(t1),
#                 "PyCPP: %0.3es"%(t2)],
#                loc="lower right")
#     plt.show()
# =============================================================================
