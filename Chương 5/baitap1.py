# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 01:55:26 2024

@author: NGUYEN THI NHU Y
"""

danhsachso = []
for so in range(2018,2829):
    if so % 2 == 0 and so % 5 == 0:
        danhsachso.append(so)
print("Danh sách số chẵn và chia hết cho 5: ")
print(danhsachso)