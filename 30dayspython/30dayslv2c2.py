# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:10:54 2024

@author: Vivobook
"""

tongchan = 0
tongle = 0
for i in range(101):
    if i % 2 == 0:
        tongchan +=i
    elif i % 2 != 0:
        tongle += i
print("Tổng tất cả số chẵn: ", tongchan)
print("Tổng tất cả số lẻ: ", tongle)