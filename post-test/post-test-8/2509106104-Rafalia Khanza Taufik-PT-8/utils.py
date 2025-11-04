import os
from prettytable import PrettyTable

def bersihkan_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_tabel_bunga(kumpulan_bunga):
    if not kumpulan_bunga:
        print("Masih kosong nih, belum ada bunga...")
        return
    table = PrettyTable()
    table.field_names = ["No", "Nama Bunga", "Harga (Rp)", "Stok", "Warna"]
    nomor = 1
    for nama, data in kumpulan_bunga.items():
        table.add_row([nomor, nama, f"{data['harga']:,}", data["stok"], data["warna"]])
        nomor += 1
    print(table)
