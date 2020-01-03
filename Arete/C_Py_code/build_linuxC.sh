#!/bin/bash
# compile source
gcc -c -fPIC ./adder.c -o ./adder.o
# link into shared object
g++ -shared ./adder.o -o ./libpycpp.so
# remove intermediary
rm ./adder.o
