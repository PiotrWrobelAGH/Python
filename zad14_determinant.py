#!/usr/bin/env python
from random import random
def complement_matrix(A, i, j):
    C = A[:i] + A[i+1:]
    for d in range(len(C)):
        C[d] = C[d][:j] + C[d][j+1:]
    return C
def det(A):
    if(len(A[0]) != len(A)):
        print('Matrix not square')
        return None
    mysum = 0
    for i in range(len(A[0])):
        if(len(A[0]) == 1):
            return A[0][0]
        mysum = mysum + A[0][i]*(-1)**i*det(complement_matrix(A, 0, i))
    return mysum

A = [[round(random()*100) for j in range(4)] for i in range(4)]

print(det(A))
