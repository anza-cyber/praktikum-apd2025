import os

print("""
     =======================================================
     |      Selamat Datang di Toko Bunga Hias Rafalia      |
     |               Daftar Dulu Yuk!                      |
     =======================================================
    """)

data_pengguna = {}
kumpulan_bunga = {}

while True:
    nama = input("Buat nama: ")
    if nama in data_pengguna:
        print("Yah namanya ada yang make... coba nama yang lain")
    else:
        password = input("Buat password: ")
        role = input("Mau daftar sebagai apa? (admin/pelanggan): ").lower()

        if role not in ["admin", "pelanggan"]:
            print("Pilihannya cuma admin atau pelanggan ya! Gak ada yang lain")
            continue
        data_pengguna[nama] = {"password": password, "role": role}
        print(f"Yeay! Akun {nama} berhasil dibuat!")
        break

percobaan_login = 0
while percobaan_login < 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("================= Login Toko Bunga Hias Rafalia =========================")
    input_nama = input("Nama : ")
    input_password = input("Password : ")

    if input_nama in data_pengguna and data_pengguna[input_nama]["password"] == input_password:
        pengguna_ditemukan = data_pengguna[input_nama]
    else:
        pengguna_ditemukan = None

    if pengguna_ditemukan:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Login berhasil! Hai {input_nama} :)")

        if pengguna_ditemukan["role"] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""
                    ==================================================
                    [         TOKO BUNGA HIAS RAFALIA - ADMIN        ]
                    ==================================================
                    [1. Tambah Bunga Baru                            ]
                    [2. Lihat Semua Bunga                            ]
                    [3. Edit Data Bunga                              ]
                    [4. Hapus Bunga                                  ]
                    [0. Logout                                       ]
                    ===================================================
                    """)

                pilihan = input("Mau ngapain? (0-4): ")
                if pilihan == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- Tambah Bunga Baru ---")
                    nama = input("Nama bunga: ")
                    harga = input("Harganya: Rp ")
                    stok = input("Stok tersedia: ")
                    warna = input("Warna: ")
                    if not harga.isdigit() or not stok.isdigit():
                        print("Harga sama stok harus pake angka!")
                        input("Tekan enter buat lanjut...")
                        continue
                    kumpulan_bunga[nama] = {
                        "harga": int(harga),
                        "stok": int(stok),
                        "warna": warna
                    }
                    print(f"Bunga {nama} udah ditambahin!")
                    input("Tekan enter buat lanjut...")

                elif pilihan == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- Daftar Bunga di Rafalia ---")
                    if not kumpulan_bunga:
                        print("Masih kosong nih, belum ada bunga...")
                    else:
                        for i, (key, bunga) in enumerate(kumpulan_bunga.items(), 1):
                            print(f"\n{i}. {key}")
                            print(f"   Harga: Rp {bunga['harga']:,}")
                            print(f"   Stok: {bunga['stok']}")
                            print(f"   Warna: {bunga['warna']}")
                    input("\nTekan enter buat lanjut...")

                elif pilihan == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- Edit Data Bunga ---")
                    if not kumpulan_bunga:
                        print("Belum ada bunga yang bisa diedit...")
                        input("Tekan enter buat lanjut...")
                        continue

                    for i, key in enumerate(kumpulan_bunga.keys(), 1):
                        print(f"{i}. {key}")

                    nama_edit = input("Masukkan nama bunga yang mau diedit: ")
                    if nama_edit not in kumpulan_bunga:
                        print("Bunga tidak ditemukan!")
                        input("Tekan enter buat lanjut...")
                        continue

                    bunga = kumpulan_bunga[nama_edit]
                    print(f"\nEdit data: {nama_edit}")
                    nama_baru = input(f"Nama baru [{nama_edit}]: ") or nama_edit
                    harga_baru = input(f"Harga baru [Rp {bunga['harga']}]: ")
                    stok_baru = input(f"Stok baru [{bunga['stok']}]: ")
                    warna_baru = input(f"Warna baru [{bunga['warna']}]: ") or bunga['warna']

                    if nama_baru != nama_edit:
                        kumpulan_bunga[nama_baru] = kumpulan_bunga.pop(nama_edit)
                        bunga = kumpulan_bunga[nama_baru]

                    if harga_baru.isdigit():
                        bunga["harga"] = int(harga_baru)
                    if stok_baru.isdigit():
                        bunga["stok"] = int(stok_baru)
                    bunga["warna"] = warna_baru

                    print("Data berhasil diupdate!")
                    input("Tekan enter buat lanjut...")

                elif pilihan == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- Hapus Bunga ---")
                    if not kumpulan_bunga:
                        print("Belum ada bunga yang bisa dihapus...")
                        input("Tekan enter buat lanjut...")
                        continue

                    for i, key in enumerate(kumpulan_bunga.keys(), 1):
                        print(f"{i}. {key}")

                    nama_hapus = input("Masukkan nama bunga yang mau dihapus: ")
                    if nama_hapus not in kumpulan_bunga:
                        print("Bunga tidak ditemukan!")
                        input("Tekan enter buat lanjut...")
                        continue

                    konfirmasi = input(f"Yakin mau hapus {nama_hapus}? (y/n): ").lower()
                    if konfirmasi == 'y':
                        del kumpulan_bunga[nama_hapus]
                        print(f"Bunga {nama_hapus} udah dihapus!")
                    else:
                        print("Penghapusan dibatalkan")

                    input("Tekan enter buat lanjut...")

                elif pilihan == "0":
                    print("Sampai jumpa lagi!")
                    break

                else:
                    print("Pilihan nggak valid, coba lagi...")

        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""
                    ==================================================
                    [    TOKO BUNGA HIAS RAFALIA - PELANGGAN         ]
                    ==================================================
                    [1. Lihat Katalog Bunga                          ]
                    [2. Cari Bunga Favorit                           ]
                    [3. Beli Bunga                                   ]
                    [0. Keluar                                       ]
                    ===================================================
                    """)

                pilihan = input("Mau apa? (0-3): ")

                if pilihan == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- Katalog Bunga Rafalia ---")
                    if not kumpulan_bunga:
                        print("Maaf, lagi kosong nih...")
                    else:
                        for i, (key, bunga) in enumerate(kumpulan_bunga.items(), 1):
                            print(f"\n{i}. {key}")
                            print(f"   Harga: Rp {bunga['harga']:,}")
                            print(f"   Stok: {bunga['stok']}")
                            print(f"   Warna: {bunga['warna']}")
                    input("\nTekan enter buat lanjut...")

                elif pilihan == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- Cari Bunga ---")
                    if not kumpulan_bunga:
                        print("Belum ada bunga nih...")
                        input("Tekan enter buat lanjut...")
                        continue

                    keyword = input("Cari bunga apa? ").lower()
                    hasil_cari = {k: v for k, v in kumpulan_bunga.items() if keyword in k.lower()}

                    if hasil_cari:
                        print(f"\nDitemukan {len(hasil_cari)} bunga:")
                        for k, v in hasil_cari.items():
                            print(f"- {k} (Rp {v['harga']:,}) - Stok: {v['stok']}")
                    else:
                        print("Bunga yang dicari nggak ketemu...")

                    input("\nTekan enter buat lanjut...")

                elif pilihan == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("--- Beli Bunga ---")
                    if not kumpulan_bunga:
                        print("Lagi kosong, nggak bisa beli...")
                        input("Tekan enter buat lanjut...")
                        continue

                    print("Bunga yang tersedia:")
                    for i, (key, bunga) in enumerate(kumpulan_bunga.items(), 1):
                        if bunga["stok"] > 0:
                            print(f"{i}. {key} - Rp {bunga['harga']:,} (Stok: {bunga['stok']})")

                    nama_beli = input("\nMau beli bunga apa? (nama): ")
                    if nama_beli not in kumpulan_bunga:
                        print("Bunga tidak ditemukan!")
                        input("Tekan enter buat lanjut...")
                        continue

                    bunga_dipilih = kumpulan_bunga[nama_beli]
                    if bunga_dipilih["stok"] == 0:
                        print("Stok bunga ini habis!")
                        input("Tekan enter buat lanjut...")
                        continue

                    jumlah = input(f"Mau beli berapa {nama_beli}? ")
                    if not jumlah.isdigit() or int(jumlah) <= 0:
                        print("Jumlah harus angka dan lebih dari 0!")
                        input("Tekan enter buat lanjut...")
                        continue

                    jumlah = int(jumlah)
                    if jumlah > bunga_dipilih["stok"]:
                        print(f"Stok tidak cukup! Cuma ada {bunga_dipilih['stok']}")
                        input("Tekan enter buat lanjut...")
                        continue

                    total = bunga_dipilih["harga"] * jumlah
                    kumpulan_bunga[nama_beli]["stok"] -= jumlah

                    print(f"\n Pembelian berhasil! ")
                    print(f"Bunga  : {nama_beli}")
                    print(f"Jumlah : {jumlah}")
                    print(f"Total  : Rp {total:,}")
                    print("Terima kasih udah belanja di Rafalia!")

                    input("\nTekan enter buat lanjut...")

                elif pilihan == "0":
                    print("Makasih udah mampir! Sampai jumpa lagi")
                    break

                else:
                    print("Pilihan nggak valid...")

        continue

    else:
        print("Login gagal. Nama atau password salah.")
        percobaan_login += 1
        if percobaan_login < 3:
            print(f"Kesempatan mencoba tinggal {3 - percobaan_login} lagi")
        input("Tekan enter buat coba lagi...")

if percobaan_login == 3:
    print("Terlalu banyak percobaan login. Coba lagi nanti ya!")