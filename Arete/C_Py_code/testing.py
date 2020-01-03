# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:05:30 2019

@author: sreynolds
"""
import timeit

cy = timeit.timeit('example_cy.test(5)', setup = 'import example_cy', number = 10000)
py = timeit.timeit('example_py.test(5)', setup = 'import example_py', number = 10000)

print(cy,py)
print('Cython is {}x faster'.format(py/cy))