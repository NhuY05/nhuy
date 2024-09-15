# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:00:41 2024

@author: NGUYEN THI NHU Y
"""

danhsachso = []
for so in range(2020,3839):
    if so % 2 == 0:
        danhsachso.append(so)
print("Danh sách các số chẵn [2020,3838]: ")
print(danhsachso)

print("Câu 1: ")
chiahet9 = []
for a in danhsachso:
    if a % 9 == 0:
        chiahet9.append(a)
print("Danh sách các số chẵn chia hết cho 9: ")
print(chiahet9)

print("Câu 2: ")
print("\t".join(map(str, chiahet9)))