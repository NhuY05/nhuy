# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:12:49 2024

@author: NGUYEN THI NHU Y
"""
#3a
import random
a = random.randint(1,11)
print("Số lượng pt ngẫu nhiên: ", a)
for i in range(a): 
    b = random.randint(20,31)
    print(b)
#3b
import random
soluongphantu = random.randint(1,82)
print("Số lượng số được chọn ngẫu nhiên: ", soluongphantu)
binhphuong = []
for songaunhien in range(soluongphantu):
    songaunhien = random.uniform(18,99)
    binhphuong.append(songaunhien ** 2)
print("Danh sách các giá trị bình phương: ", binhphuong)
    