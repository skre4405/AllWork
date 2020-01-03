# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:57:33 2019

@author: sreynolds
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cy.pyx'))