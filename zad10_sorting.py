#!/usr/bin/env python
from random import random

lista = [None]*50
lista_sorted = [None]*50
for i in range(0, 50):
    lista[i] = random()
smallest = None
for i in range(0, 50):
    for x in range(0, 50):
        if(lista[x] == None):
            continue
        if(smallest == None or smallest>lista[x]):
            smallest = lista[x]
    lista_sorted[i] = smallest
    lista[lista.index(smallest)] = None
    smallest = None
for i in range(0, 50):
    print(lista_sorted[i])