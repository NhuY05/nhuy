# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:57:14 2024

@author: NGUYEN THI NHU Y
"""
import random
chon = ("Kéo", "Búa", "Bao")
may = random.choice(chon)
nguoi = input("Chọn kéo, búa hoặc bao: ")
print("Máy chọn: ", may)
if nguoi == may:
    print("Hòa")
elif nguoi == "Kéo" and may == "Bao" or\
     nguoi == "Búa" and may == "Kéo" or\
     nguoi == "Bao" and may == "Búa":
     print("Người chơi thắng")
else:
    print("Người chơi thua")