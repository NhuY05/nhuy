# km-*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:44:36 2024

@author: NGUYEN THI NHU Y
"""
while True:
    km = int(input("Km đã đi: "))
    if km < 0:
        print("Km không hợp lệ, vui lòng nhập lại")
        continue
    break
tien = 0
for km in range(1, km + 1):
    if km == 1:
        tien += 15000
    elif 2 <= km <= 5:
        tien += 13500
    elif 6 <= km <= 120:
        tien += 11000
    if km > 120:
        tien *= 0.9
print("Tổng tiền cho: ", km, "km là", tien )
