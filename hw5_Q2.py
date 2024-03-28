# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:21:02 2024

@author: LAM Quincy
"""
n=100
i=2
for i in range(2,n):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,'',end='')
    