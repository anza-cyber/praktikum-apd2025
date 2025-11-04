from utils import bersihkan_terminal
from data_store import data_pengguna

def register():
    while True:
        bersihkan_terminal()
        print("""
     =======================================================
     |                   MENU REGISTRASI                   |
     =======================================================
        """)
        nama = input("Buat nama: ")
        if nama in data_pengguna:
            print("Yah namanya sudah ada yang make... coba nama yang lain deh")
            input("Tekan enter buat lanjut...")
            continue
        else:
            password = input("Buat password: ")
            role = input("Mau daftar sebagai apa nih? (admin/pelanggan): ")

            if role != "admin" and role != "pelanggan":
                print("Pilihannya cuma admin atau pelanggan ya! gak ada yang lain")
                input("Tekan enter buat lanjut...")
                continue

            data_pengguna[nama] = {
                "password": password,
                "role": role
            }
            pesan_berhasil = f"Yeay! Akun {nama} berhasil dibuat!"
            point_awal = 100 if role == "pelanggan" else 0
            print(pesan_berhasil)
            if role == "pelanggan":
                print(f"Kamu dapat {point_awal} point")
            input("Tekan enter buat lanjut...")
            break
