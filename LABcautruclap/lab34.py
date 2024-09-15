# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:22:40 2024

@author: NGUYEN THI NHU Y
"""
import math
while True:
    N = int(input('Nhập số nguyên dương: '))
    if N < 0:
            print("Vui lòng nhập nguyên dương")
            continue
    break
if N > 1:
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            print("N không là số nguyên tố")
            break
    else:
        print("N là số nguyên tố")
else:
        print("N không phải số nguyên tố")