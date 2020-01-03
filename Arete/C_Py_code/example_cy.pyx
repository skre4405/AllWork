# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:45:19 2019

@author: sreynolds
"""
cpdef int test(int x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y+= i
    return y