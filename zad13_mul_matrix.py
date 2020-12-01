#!/usr/bin/env python

f = [[2 for j in range(25)] for i in range(50)]
g = [[2 for j in range(100)] for i in range(25)]

def mul_matrix(a, b):
    if(len(a[0]) != len(b)):
        print('Wrong matrix size')
        return -1
    c = [[0]*len(b[0])]*len(a)
    for i in range(len(a)):
        for j in range(len(b[0])):
            mysum = 0
            for x in range(len(a[0])):
                mysum = mysum + a[i][x] * b[x][j]
            c[i][j] = mysum    
    return c

d = mul_matrix(f,g)