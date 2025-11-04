from utils import bersihkan_terminal, tampilkan_tabel_bunga
from data_store import kumpulan_bunga, data_pengguna, jumlah_pengunjung
from prettytable import PrettyTable

def hitung_total_pembelian():
    total = 0
    for bunga in kumpulan_bunga.values():
        total += bunga["harga"] * 10
    return total

def hitung_faktorial(angka):
    if angka == 1 or angka == 0:
        return 1
    elif angka < 0:
        return "Gak bisa hitung faktorial dong kalo angka negatif"
    else:
        return angka * hitung_faktorial(angka - 1)

def tampilkan_jumlah_pengguna():
    admin_count = 0
    pelanggan_count = 0
    for user in data_pengguna.values():
        if user["role"] == "admin":
            admin_count += 1
        else:
            pelanggan_count += 1
    print(f"Total Admin: {admin_count}")
    print(f"Total Pelanggan: {pelanggan_count}")

def tampilkan_info_toko():
    bersihkan_terminal()
    print("=== INFO TOKO RAFALIA ===")
    tampilkan_jumlah_pengguna()
    total_nilai = hitung_total_pembelian()
    print(f"Total nilai stok: Rp {total_nilai:,}")
    print(f"Pengunjung hari ini: {jumlah_pengunjung}")
    print(f"\nBonus: 5! = {hitung_faktorial(5)}")
    input("\nTekan enter buat lanjut...")

def tambah_bunga():
    bersihkan_terminal()
    print("--- Tambah Bunga Baru ---")
    nama_bunga = input("Nama bunga: ")
    try:
        harga = int(input("Harganya: Rp "))
        stok = int(input("Stok tersedia: "))
    except ValueError:
        print("Harga dan stok harus angka!")
        input("Tekan enter buat lanjut...")
        return
    warna = input("Warna: ")
    if harga <= 0 or stok < 0:
        print("Harga harus lebih dari 0 ya! dan stok gak boleh negatif!")
        input("Tekan enter buat lanjut...")
        return
    kumpulan_bunga[nama_bunga] = {"harga": harga, "stok": stok, "warna": warna}
    print(f"Bunga {nama_bunga} udah ditambahin!")
    input("Tekan enter buat lanjut...")

def edit_bunga():
    bersihkan_terminal()
    print("--- Edit Data Bunga ---")
    if not kumpulan_bunga:
        print("Belum ada data bunga.")
        input("Enter untuk lanjut...")
        return

    tampilkan_tabel_bunga(kumpulan_bunga)
    nama = input("Masukkan nama bunga yang ingin diubah: ")

    if nama not in kumpulan_bunga:
        print("Bunga tidak ditemukan.")
        input("Enter untuk lanjut...")
        return

    print(f"Data bunga saat ini: {kumpulan_bunga[nama]}")
    nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
    harga_baru = input("Harga baru (kosongkan jika tidak diubah): ")
    stok_baru = input("Stok baru (kosongkan jika tidak diubah): ")
    warna_baru = input("Warna baru (kosongkan jika tidak diubah): ")

    if nama_baru:
        kumpulan_bunga[nama_baru] = kumpulan_bunga.pop(nama)
        nama = nama_baru
    if harga_baru:
        kumpulan_bunga[nama]["harga"] = int(harga_baru)
    if stok_baru:
        kumpulan_bunga[nama]["stok"] = int(stok_baru)
    if warna_baru:
        kumpulan_bunga[nama]["warna"] = warna_baru

    print("Data bunga berhasil diubah!")
    input("Enter untuk lanjut...")

def hapus_bunga():
    bersihkan_terminal()
    print("--- Hapus Bunga ---")
    if not kumpulan_bunga:
        print("Belum ada data bunga.")
        input("Enter untuk lanjut...")
        return

    tampilkan_tabel_bunga(kumpulan_bunga)
    nama = input("Masukkan nama bunga yang ingin dihapus: ")

    if nama not in kumpulan_bunga:
        print("Bunga tidak ditemukan.")
        input("Enter untuk lanjut...")
        return

    konfirmasi = input(f"Yakin ingin menghapus {nama}? (y/n): ")
    if konfirmasi.lower() == "y":
        del kumpulan_bunga[nama]
        print(f"Bunga {nama} berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
    input("Enter untuk lanjut...")

def menu_admin():
    while True:
        bersihkan_terminal()
        print(f"""
        ==================================================
        [         TOKO BUNGA HIAS RAFALIA - ADMIN        ]
        ==================================================
        [1. Tambah Bunga Baru                           ]
        [2. Lihat Semua Bunga                           ]
        [3. Edit Data Bunga                             ]
        [4. Hapus Bunga                                 ]
        [5. Lihat Info Toko                             ]
        [0. Logout                                      ]
        ===================================================
        """)
        pilihan = input("Mau ngapain? (0-5): ")
        if pilihan == "1":
            tambah_bunga()
        elif pilihan == "2":
            bersihkan_terminal()
            print("--- Daftar Bunga di Toko Rafalia ---")
            tampilkan_tabel_bunga(kumpulan_bunga)
            input("\nTekan enter buat lanjut...")
        elif pilihan == "3":
            edit_bunga()
        elif pilihan == "4":
            hapus_bunga()
        elif pilihan == "5":
            tampilkan_info_toko()
        elif pilihan == "0":
            print("Sampai jumpa lagi ya!")
            return
        else:
            print("Pilihan gak valid, coba lagi...")
            input("Tekan enter buat lanjut...")