# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:22:34 2024

@author: Vivobook
"""
kitudacbiet = ["!", "@", "#", "$", "%", "^", "&","*","(",")","-","+","="]

while True:
    ID = input("Nhập ID user của bạn: ")
    if len(ID) < 6 or len(ID) > 24:
        print("ID không hợp lệ. Vui lòng nhập ID có ít nhất 6 kí tự và tối đa 24 kí tự")
    elif ID in kitudacbiet:
        print("ID không hợp lệ do chứa kí tự đặc biệt")
    elif " " in ID:
        print("ID không hợp lệ do chứa khoảng trắng")
    else:
        print("ID hợp lệ")
        break  
while True:
    password = input("Nhập password của bạn: ")
    if len(password) < 6 or len(password) > 24:
        print("Mật khẩu không hợp lệ. Vui lòng nhập mk có từ 6-24 kí tự")
        continue  
    thuong = False
    hoa = False
    so = False
    dacbiet = False
    kitudacbiet = ["!", "@", "#", "$", "%", "^", "&","*","(",")","-","+","="]
    for a in password:
        if a.islower():
            thuong = True
        elif a.isupper():
            hoa = True
        elif a.isdigit():
            so = True
        elif a in kitudacbiet:
            dacbiet = True
    if not thuong:
        print("MK không hợp lệ, cần ít nhất 1 chữ thường")
    elif not hoa: 
        print("MK không hợp lệ, cần ít nhất 1 chữ hoa")
    elif not so:
        print("MK không hợp lệ, cần ít nhất 1 số")
    elif not dacbiet:
        print("MK không hợp lệ, cần ít nhất 1 kí tự đặc biệt")
    else:
        print("Pass hợp lệ")
        break
