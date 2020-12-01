#!/usr/bin/env python
from random import random

a = [[0 for j in range(128)] for i in range(128)]
b = [[0 for j in range(128)] for i in range(128)]
c = [[0 for j in range(128)] for i in range(128)]

for i in range(128):
    for j in range(128):
        a[i][j] = random()
        b[i][j] = random()
        c[i][j] = a[i][j] + b[i][j]