# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:29:01 2024

@author: NGUYEN THI NHU Y
"""
n = int(input("Nhập n: "))
S = 0
for i in range(n+1):
    S += 1 / (2*i +1)
print("Kết quả: ", S)