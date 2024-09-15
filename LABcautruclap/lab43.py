# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:03:32 2024

@author: NGUYEN THI NHU Y
"""

n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += i/(i+1)
print("Kết quả: ", S)