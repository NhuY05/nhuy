# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:24:21 2024

@author: Vivobook
"""
import random
#Người mua vé
while True:
    somoive = []
    
#Số vé   
    sove = int(input("Số vé bạn muốn mua: "))
    if sove < 1:
        print("Số vé phải lớn hơn 0")
        continue
    
    for i in range(sove):
        so = set()
        print(f"\nChọn 6 số cho vé số {i + 1}: ")
    
        while len(so) < 6:
            num = (int(input("Chọn 6 số bất kì từ 1-45: ")))
            if 1 <= num <= 45:
                so.add(num)
            
            else:
                print("Vui lòng nhập số từ 1-45")
        somoive.append(so)
    break
#Giá vé
gia = 10000
tongtien = sove * gia

#Máy xổ số
sotrung = random.sample(range(1, 46), 6)
print("Dãy số trúng thưởng","-".join(map(str,sotrung)))

#Kết quả
sogiong = len(so.intersection(sotrung))

#tiền
mucthuong = [0, 0, 0, 30000, 300000, 10000000, 10000000000]
tientrungthuong = mucthuong[sogiong] * sove

print("Tổng tiền mua vé số: ", tongtien)
print("Tổng số tiền trúng thưởng: ", tientrungthuong)



 