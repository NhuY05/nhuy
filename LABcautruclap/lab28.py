# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 03:06:37 2024

@author: Vivobook
"""

while True:
    try:
        N = int(input("Nhập số nguyên dương: "))
        if N > 0:
            print("Số đã nhập: ", N)
            break
        else:
            print("Không phải số nguyên dương, nhập lại")
    except:
        print("Vui lòng nhập số")
for a in range(1, N + 1):
        if N % a == 0:
            print("Các ước số của N: ", a)