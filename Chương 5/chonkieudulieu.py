# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:40:38 2024

@author: Vivobook
"""

class NVVanPhong:
    def __init__(self, ma_nhan_vien, ho_ten, luong_co_ban, luong_hang_thang, so_ngay):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.luong_hang_thang = luong_hang_thang
        self.so_ngay = so_ngay

class NVBanHang:
    def __init__(self, ma_nhan_vien, ho_ten, luong_co_ban, luong_hang_thang, so_san_pham):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.luong_hang_thang = luong_hang_thang
        self.so_san_pham = so_san_pham

# Khởi tạo dữ liệu cho 10 nhân viên
nhan_vien = [
    NVVanPhong("VP001", "Nguyễn Văn A", 5000000, 7000000, 22),
    NVVanPhong("VP002", "Trần Thị B", 6000000, 8000000, 20),
    NVVanPhong("VP003", "Lê Văn C", 5500000, 7500000, 21),
    NVVanPhong("VP004", "Phạm Thị D", 6500000, 8500000, 23),
    NVBanHang("BH001", "Nguyễn Văn E", 4000000, 6000000, 30),
    NVBanHang("BH002", "Trần Thị F", 4500000, 6500000, 25),
    NVBanHang("BH003", "Lê Văn G", 5000000, 7000000, 20),
    NVBanHang("BH004", "Phạm Thị H", 5500000, 7500000, 28),
    NVVanPhong("VP005", "Vũ Văn I", 7000000, 9000000, 24),
    NVBanHang("BH005", "Nguyễn Thị J", 4800000, 6800000, 22)
]

# In thông tin nhân viên
for nv in nhan_vien:
    print("Mã nhân viên:", nv.ma_nhan_vien, 
          ", Họ và tên:", nv.ho_ten, 
          ", Lương cơ bản:", nv.luong_co_ban, 
          ", Lương hàng tháng:", nv.luong_hang_thang)