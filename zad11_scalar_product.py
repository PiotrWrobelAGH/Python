#!/usr/bin/env python

a = [1,2,12,4]
b = [2,4,2,8]
c = [0]*4
sum = 0
for i in range(len(a)):
    c[i] = a[i]*b[i]
    sum = sum + c[i]
print(sum)
