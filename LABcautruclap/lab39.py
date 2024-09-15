# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:14:55 2024

@author: NGUYEN THI NHU Y
"""
n = int(input("Nhập số n: "))
S = 0
for i in range(1, n+1):
    S += 1/i
print("Kết quả: ", S)
