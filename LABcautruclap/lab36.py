# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:48:15 2024

@author: NGUYEN THI NHU Y
"""
#36
while True:
    n = int(input("Nhập số nguyên dương: "))
    if n < 1:
        print("Vui lòng nhập số nguyên dương")
        continue
    break
S = n*(n+1) * (2*n + 1) // 6
print("Tổng bình phương là: ", S)