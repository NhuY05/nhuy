# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:05:38 2024

@author: NGUYEN THI NHU Y
"""
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += (2*i+1)/(2*i+2)
print("Kết quả: ", S)
