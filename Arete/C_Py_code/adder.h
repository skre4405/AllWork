
/*# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:48:59 2019

@author: sreynolds
"""
*/
#ifndef __PYCPP_ADDER_H__
#define __PYCPP_ADDER_H__

#include <stdint.h>
#include <stddef.h>
//using std::size_t;


// implementation
template<typename T>
void adder(T const *a, T const *b, T *out, size_t n);

// C interface for Python
extern "C"
{

void adder_f(float const *a, float const *b, float *out, size_t n);

void adder_d(double const *a, double const *b, double *out, size_t n);

} // extern "C"

#endif // __PYCPP_ADDER_H__

