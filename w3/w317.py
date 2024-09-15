# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:44:33 2024

@author: NGUYEN THI NHU Y

"""

n = int(input("Nhập số nguyên n: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()