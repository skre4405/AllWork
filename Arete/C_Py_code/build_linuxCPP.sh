#!/bin/bash
# compile source
g++ -c -std=c++11 -O2 -fPIC -I. ./adder.cpp -o ./adder.o
# link into shared object
g++ -shared ./adder.o -o ./libpycpp.so
# remove intermediary
rm ./adder.o
