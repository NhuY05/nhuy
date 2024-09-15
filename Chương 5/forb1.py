# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:55 2024

@author: NGUYEN THI NHU Y
"""

print("Bài 1 for")
n = int(input("Nhập 1 số nguyên dương: "))
giaithua = 1
for i in range(1, n + 1):
    giaithua *= i
print("Giai thừa của ", n, "là: ", giaithua)