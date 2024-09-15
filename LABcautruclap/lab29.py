# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:57:15 2024

@author: NGUYEN THI NHU Y
"""

N = int(input("Nhập số nguyên dương: "))
tong = 0
while N > 0:
    so = N % 10
    tong += so
    N //= 10
print("Tổng các chữ số là: ", tong)


