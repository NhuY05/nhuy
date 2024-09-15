# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:16:13 2024

@author: NGUYEN THI NHU Y
"""

str_input = input("Nhập chuỗi: ")
dodaichuoi = len(str_input)
print("Độ dài chuỗi: ", dodaichuoi)
kitudacbiet = 0
kituthuong = 0
kituso = 0
kituhoa = 0

daykitudacbiet = []
daykituthuong = []
daykituso = []
daykituhoa = []
cackitudacbiet = set("!@#$%^&*()-=+/")

for kitu in str_input:
    if kitu in cackitudacbiet:
        kitudacbiet += 1
        daykitudacbiet.append(kitu)
    elif kitu.islower():
        kituthuong += 1
        daykituthuong.append(kitu)
    elif kitu.isdigit():
        kituso += 1
        daykituso.append(kitu)
    elif kitu.isupper():
        kituhoa += 1
        daykituhoa.append(kitu)
print("Số kí tự đặt biệt: ", kitudacbiet, "Các ký tự đó là: ", ",".join(daykitudacbiet))
print("Số kí tự [a-z]: ", kituthuong, "Các ký tự đó là: ", ",".join(daykituthuong))
print("Số kí tự [0-9]: ", kituso, "Các ký tự đó là: ", ",".join(daykituso))
print("Số kí tự [A-Z]: ", kituhoa, "Các ký tự đó là: ", ",".join(daykituhoa))