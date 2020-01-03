/*
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:40:43 2019

@author: sreynolds
*/
#include <iostream>
#include "adder.hpp"
using namespace std;

// implementation
template<typename T>
void adder(T const *a, T const *b, T *out, size_t n)
{
    for (size_t i = 0; i < n; ++i)
        out[i] = a[i] + b[i];
}

void adder_f(float const *a, float const *b, float *out, size_t n)
{
    cout<<"hello";
    return adder<float>(a, b, out, n);
    
}

void adder_d(double const *a, double const *b, double *out, size_t n)
{
    cout<<"hello";
    return adder<double>(a, b, out, n);
    
}
