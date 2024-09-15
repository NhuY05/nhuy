# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:15:19 2024

@author: NGUYEN THI NHU Y

2X + 7Y +9Z =979
Z<= 979/9 --> Z ~ 108,78
7Y <= 979 - 9Z --> Y <= 979-9Z/7
Y>0

X= 979-7Y-9Z/2
X>0 AND X LÀ SỐ NGUYÊN
x+Y+Z NHỎ NHẤT
"""
nghiemtotnhat = []
nhonhat = 1000
for z in range(1, 979 //9 + 1 ):
    for y in range(1, (979 - 9*z) // 7 + 1):
        
        x = (979 - 7*y - 9*z) // 2
        if x > 0 and x % 2 == 0:
            nghiem = [int(x), y, z]
            tongnghiem = int(x) + y + z
            
            if tongnghiem < nhonhat:
                nhonhat = tongnghiem
                nghiemtotnhat = [nghiem]
            elif tongnghiem == nhonhat:
                nghiemtotnhat.append(nghiem)
print("Tổng nghiệm: ", nhonhat)
print("Bộ nghiệm đạt tổng nhỏ nhất: ", nghiemtotnhat)