# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:05:52 2024

@author: NGUYEN THI NHU Y
"""
def namnhuan(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

songay = 0
while True:
    if thang < 1 or thang > 12:
        print("Tháng không hợp lệ. Nhập lại")
        thang = int(input("Nhập tháng: "))
        continue
    break
if thang in [1, 3, 5, 7, 8, 10, 12]:
    songay = 31
elif thang in [4, 6, 9, 11]:
    songay = 30
elif thang == 2:
    if namnhuan(year):
        songay = 29
    else:
        songay = 28
print("Tháng", thang, "Năm", nam, "có",songay, "ngày")