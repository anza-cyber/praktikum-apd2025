from utils import bersihkan_terminal
from auth import register
from admin import menu_admin
from pelanggan import menu_pelanggan
from promo import tampilkan_promo_hari_ini
from data_store import data_pengguna, jumlah_pengunjung

def login():
    percobaan_login = 0
    while percobaan_login < 3:
        bersihkan_terminal()
        print("================= Login Toko Bunga Hias Rafalia =========================")
        input_nama = input("Nama : ")
        input_password = input("Password : ")

        if input_nama in data_pengguna and data_pengguna[input_nama]["password"] == input_password:
            pengguna_ditemukan = data_pengguna[input_nama]
        else:
            pengguna_ditemukan = None

        if pengguna_ditemukan:
            bersihkan_terminal()
            nama_user = input_nama
            role_user = pengguna_ditemukan["role"]
            sambutan = f"Login berhasil! Hai {nama_user} :)"
            pesan_role = "Selamat mengelola toko!" if role_user == "admin" else "Selamat berbelanja!"
            global jumlah_pengunjung
            jumlah_pengunjung += 1
            print(sambutan)
            print(pesan_role)
            if role_user == "pelanggan":
                tampilkan_promo_hari_ini()
            input("\nTekan enter buat lanjut...")
            if role_user == "admin":
                menu_admin()
            else:
                menu_pelanggan()
            return True
        else:
            print("Login gagal. nama atau password salah.")
            percobaan_login += 1
            if percobaan_login < 3:
                print(f"Kesempatan mencoba tinggal {3 - percobaan_login} lagi")
            input("Tekan enter buat coba lagi...")

    if percobaan_login == 3:
        print("Terlalu banyak percobaan login nih. Coba lagi nanti ya!")
        input("Tekan enter buat lanjut...")
    return False


def main():
    while True:
        bersihkan_terminal()
        print("""
     =======================================================
     |                MENU UTAMA RAFALIA                  |
     =======================================================
     | [1] Register (Daftar Akun Baru)                    |
     | [2] Login (Masuk ke Akun)                          |
     | [3] Lihat Promo                                    |
     | [0] Logout                                         |
     =======================================================
        """)
        pilihan = input("Pilih menu (0-3): ")

        if pilihan == "1":
            register()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            bersihkan_terminal()
            tampilkan_promo_hari_ini()
            input("\nTekan enter buat kembali...")
        elif pilihan == "0":
            print("Terima kasih telah mengunjungi Toko Bunga Hias Rafalia!")
            break
        else:
            print("Pilihan gak valid. Silakan pilih 0-3.")
            input("Tekan enter buat lanjut...")

if __name__ == "__main__":
    main()
