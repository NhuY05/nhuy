# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:56:29 2024

@author: NGUYEN THI NHU Y
2X + 7Y +9Z =979
Z<= 979/9 --> Z ~ 108,78
7Y <= 979 - 9Z --> Y <= 979-9Z/7
Y>0

X= 979-7Y-9Z/2
X>0 AND X LÀ SỐ NGUYÊN

 
"""
lonnhat = 0
nghiemtotnhat = []
for z in range(1, 979 // 9 + 1):
    for y in range(1, (979 - 9*z) // 7 + 1):
       
        x = (979 - 7*y -9*z) // 2
        if x > 0 and x.is_integer():
            nghiem = (int(x), y, z)
 #so sánh tổng nghiệm với tổng max           
            tongnghiem = int(x) + y + z
            
            if tongnghiem > lonnhat:
                lonnhat = tongnghiem
                nghiemtotnhat = [nghiem]
            elif tongnghiem == lonnhat:
    # = nhau nên thêm vào danh sách luôn
                nghiemtotnhat.append(nghiem)
print("Tổng lớn nhất: ", lonnhat)
print("Bộ nghiệm đạt tổng lớn nhất: ",nghiemtotnhat)