# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:36:54 2024

@author: Vivobook
"""

import random


lua_chon = ['kéo', 'búa', 'bao']
ket_qua = {
    ('kéo', 'bao'): 'Người thắng',
    ('bao', 'búa'): 'Người thắng',
    ('búa', 'kéo'): 'Người thắng',
    ('bao', 'kéo'): 'Máy thắng',
    ('búa', 'bao'): 'Máy thắng',
    ('kéo', 'búa'): 'Máy thắng',
}

def choi_game(soluong_nguoi):
    diem_nguoi = [0] * soluong_nguoi
    diem_may = 0

    for i in range(soluong_nguoi):
        lua_chon_nguoi = random.choice(lua_chon)
        lua_chon_may = random.choice(lua_chon)
        
        # In kết quả
        print("Người chơi", i + 1, "ra:", lua_chon_nguoi, "- Máy ra:", lua_chon_may)

        if lua_chon_nguoi == lua_chon_may:
            ket_qua_game = "Hòa"
        else:
            ket_qua_game = ket_qua.get((lua_chon_nguoi, lua_chon_may), "Hòa")
            if ket_qua_game == 'Người thắng':
                diem_nguoi[i] += 1
            elif ket_qua_game == 'Máy thắng':
                diem_may += 1

        print("=> Kết quả:", ket_qua_game)
        print("Điểm người chơi", i + 1, ":", diem_nguoi[i], "- Điểm máy:", diem_may, "\n")

    # Tổng kết
    tong_diem_nguoi = sum(diem_nguoi)
    print("Tổng điểm người chơi:", tong_diem_nguoi)
    print("Tổng điểm máy:", diem_may)

# Chọn số lượng người chơi ngẫu nhiên từ 8 đến 20
soluong_nguoi = random.randint(8, 20)
print("Số lượng người chơi:", soluong_nguoi, "\n")

# Chơi trò chơi
choi_game(soluong_nguoi)