# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:13:37 2024

@author: LAM Quincy
"""
row=10
for i in range(1,row+1):
    for j in range(1,row+1-i):
        print('',end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()