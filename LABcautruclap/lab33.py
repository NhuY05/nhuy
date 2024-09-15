# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:07:56 2024

@author: NGUYEN THI NHU Y
"""
import math
while True:
    N = int(input("Nhập số nguyên dương: "))
    if N < 0:
        print("Vui lòng nhập số nguyên dương")
        continue
    break
canbachai = math.sqrt(N)
    
if canbachai.is_integer():
    print("N là số chính phương")
else: 
    print("N không phải số chính phương")
    