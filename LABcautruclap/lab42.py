# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:37:16 2024

@author: NGUYEN THI NHU Y
"""

n = int(input("Nhập n: "))
S=0
for i in range(1, n+1):
    S += 1/(i*(i+1))   
print("Kết quả: ", S)