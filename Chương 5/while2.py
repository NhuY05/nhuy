# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 01:49:39 2024

@author: NGUYEN THI NHU Y
"""

while True:
    try:
        giatri = float(input("Nhập 1 số thực [-89.9; 88.8]: "))
        if -89.9 <= giatri <= 88.8:
            print("Giá trị thỏa điều kiện")
            break
        else:
            print("Giá trị không thỏa điều kiện")
    except:
        print("Vui lòng nhập số")