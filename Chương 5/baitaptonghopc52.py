# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:37:02 2024

@author: NGUYEN THI NHU Y
"""

email = input("Nhập email của bạn: ")
if email.count("@") != 1:
    print("Email không hợp lệ")
else:
    truoc, sau = email.split("@")
    if len(truoc) < 6:
        print("Email không hợp lệ")
    else:
        khoangtrang = True
        kitudacbiet = True
        for i in truoc:
            if i == " ":
                khoangtrang = False
            elif not i.isalnum():
                kitudacbiet = False
        if khoangtrang == False:
            print("Mail k hợp lệ do phía trước @ chứa khoảng trắng")
        elif kitudacbiet == False:
            print("Mail không hợp lệ vì trước @ chứ kí tự đặc biệt")
        else:
            print("Mail hợp lệ")