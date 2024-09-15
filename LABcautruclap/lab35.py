# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:39:46 2024

@author: NGUYEN THI NHU Y
"""
while True:
    n = int(input("Nhập số nguyên dương: "))
    if n < 0:
        print("Vui lòng nhập số nguyên dương")
        continue
    break
#công thức tỉnh tổng
S = n * (n+1) // 2
print("Tổng: ", S)
