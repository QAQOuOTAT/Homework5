# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:23:31 2024

@author: LAM Quincy
"""

特別獎=['63603594']
特獎=['73155944']
a=['9','4','9','8','5','8','9','9']
b=['5','7','2','8','3','4','2','0']
c=['6','2','8','2','5','2','7','8']
x=input('統一發票號碼 : ')
y=[z for z in x]
if x == 特別獎:
    print('獎金1,000萬元')
if x == 特獎:
    print('獎金200萬元')
for j in[a,b,c]:
    for i in range(8,2,-1):
        if y[-i:]==j[-i:]:
            if i == 8:
                print('獎金20萬元')
                break
            elif i == 7:
                print('獎金4萬元')
                break
            elif i == 6:
                print('獎金1萬元')
                break
            elif i == 5:
                print('獎金4千元')
                break
            elif i == 4:
                print('獎金1千元')
                break
            elif i == 3:
                print('獎金2百元')
                break