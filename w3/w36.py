# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:01:56 2024

@author: Vivobook
"""
n = int(input("Nhập n, n < 1000: "))
if n < 1000:
    for i in range(n):
        print("Hello")
else:
    print("Vui lòng nhập tham số < 1000")
    