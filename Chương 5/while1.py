# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 01:27:52 2024

@author: NGUYEN THI NHU Y


"""
#while true duy trì đến khi hợp lệ
#try-except để kiểm tra lỗi nếu như kh nhập số
while True:
    try:
        giatri = float(input("Nhập giá trị trong khoảng [-99, 99]: "))
        if -99 <= giatri <= 99:
            print("Giá trị hợp lệ")
            break
        else:
            print("Giá trị không hợp lệ")
    except:
        print("Vui lòng nhập số")