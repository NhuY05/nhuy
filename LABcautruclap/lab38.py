# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:35:14 2024

@author: NGUYEN THI NHU Y
"""

while True:
    n = int(input("Nhập n là số lẻ > 0: "))
    if n <= 0 or n % 2 == 0:
        print("Hãy nhập số lẻ > 0")
        continue
    break
S= 1
for i in range(1, n+1):
    S *=i
print("Giai thừa của ",n,"là", S)