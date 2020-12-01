#!/usr/bin/env python
import os

def fun(x, string):
    dirlist = os.listdir(x)
    for i in range(0,len(dirlist)):
        if(os.path.isdir(x + f'/{dirlist[i]}')):
            print(f'{string}{dirlist[i]}')
            fun(x + f'/{dirlist[i]}', string + '---')
        else:
            print(f'{string}{dirlist[i]}')
fun(os.getcwd(), '')        
