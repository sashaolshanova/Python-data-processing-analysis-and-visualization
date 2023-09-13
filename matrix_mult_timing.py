#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 09:54:48 2021

@author: majort
Compare simple and NUmPy matrix multiplication
"""

import timeit
import numpy as np
from random import seed
from random import random

def for_matrix(m1, m2, m):
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m[i][j] += m1[i][k] * m2[k][j]
    
def numpy_matrix(m1, m2, m):
    m = np.dot(m1, m2)
    
def main():
    n1 = 400
    n2 = 400
    m1 = []
    m2 = []
    m = []
    seed(1)
    m1 = [[random() for i in range(n1)] for j in range(n2)]
    m2 = [[random() for i in range(n1)] for j in range(n2)]
    m = [[0 for i in range(n1)] for j in range(n2)]
    print("for matrix mult\t\t\t", timeit.timeit(lambda: for_matrix(m1, m2, m), number=1))
    print("numpy matrix mult\t\t", timeit.timeit(lambda: numpy_matrix(m1, m2, m), number=1))

if __name__ == '__main__':
    main()
    
