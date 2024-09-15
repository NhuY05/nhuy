# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:20:18 2024

@author: NGUYEN THI NHU Y

#2X + 7Y + 9Z = 979

#9Z <= 979 --> z =979/9 ~ 108,78 
#7Y = 979 - 9Z- 2X
7Y>0 --> 979 -9Z -2X > 0 --> X = 979 - 9Z / 2



"""
for z in range(1, 979 // 9 +1):
    for y in range(1, (979 - 9*z)//7 + 1):
        
        x = (979 - 7 * y - 9 * z)/2
        
    if x > 0 and x.is_integer():
        print("Nghiệm của phương trình: ", "x= ",int(x), "y=",y,"z=",z)