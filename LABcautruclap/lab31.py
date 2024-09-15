# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:26:20 2024

@author: NGUYEN THI NHU Y
"""
while True:
        a = int(input("Nhập số nguyên dương thứ 1: "))
        b = int(input("Nhập số nguyên dương thứ 2: "))
        c = int(input("Nhập số nguyên dương thứ 3: "))
        if a <= 0 or b <= 0 or c <= 0:
            print("Vui lòng nhập số nguyên dương")
            continue
        break

if a + b > c and a + c > b and b + c > a:
    print("3 số có thể lập thành tam giác")
else:
    print("3 số không thể lập thành tam giác")


if a == b == c:
    print("Tam giác đều")
elif a == b or b == c or a == c:
    print("Tam giác cân")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2:
    print("Tam giác vuông")
else:
    print("Tam giác thường")

