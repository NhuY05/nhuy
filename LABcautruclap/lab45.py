# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:08:31 2024

@author: NGUYEN THI NHU Y
"""

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += (x**i)/(i*(i+1)/2)
print("Kết quả: ", S)