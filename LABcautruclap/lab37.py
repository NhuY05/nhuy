# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:26:51 2024

@author: NGUYEN THI NHU Y
"""

while True:
    n = int(input("Nhập n nguyên và lớn hơn 0: "))
    if n <= 0 or n % 2 != 0:
        print("Vui lòng nhập n > 0 và chia hết cho 2")
        continue
    break
S = n *(n+2)//4
print("Tổng: ", S)
