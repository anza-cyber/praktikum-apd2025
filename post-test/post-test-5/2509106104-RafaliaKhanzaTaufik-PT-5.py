import os

print("""
     =======================================================
     |      Selamat Datang di Toko Bunga Hias Rafalia      |
     =======================================================
    """)

data_pengguna = []
kumpulan_bunga = []

def register():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
     =======================================================
     |                   MENU REGISTRASI                   |
     =======================================================
        """)
        nama = input("Buat nama: ")
        for pengguna in data_pengguna:
            if pengguna[0] == nama:
                print("Yah namanya ada yang make... coba nama yang lain")
                input("Tekan enter buat lanjut...")
                break
        else:
            password = input("Buat password: ")
            role = input("Mau daftar sebagai apa? (admin/pelanggan): ").lower()
            
            if role not in ["admin", "pelanggan"]:
                print("Pilihannya cuma admin atau pelanggan ya! gak ada yang lain")
                input("Tekan enter buat lanjut...")
                continue
            data_pengguna.append([nama, password, role])
            print(f"Yeay! Akun {nama} berhasil dibuat!")
            input("Tekan enter buat lanjut...")
            break

def login():
    percobaan_login = 0
    while percobaan_login < 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("================= Login Toko Bunga Hias Rafalia =========================")
        input_nama = input("nama : ")
        input_password = input("Password : ")    
        pengguna_ditemukan = None
        for pengguna in data_pengguna:
            if pengguna[0] == input_nama and pengguna[1] == input_password:
                pengguna_ditemukan = pengguna
                break
        
        if pengguna_ditemukan:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Login berhasil! Hai {input_nama} :)")       
            if pengguna_ditemukan[2] == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
                    ==================================================
                    [         TOKO BUNGA HIAS RAFALIA - ADMIN            ]
                    ==================================================
                    [1. Tambah Bunga Baru                           ]
                    [2. Lihat Semua Bunga                           ]
                    [3. Edit Data Bunga                             ]
                    [4. Hapus Bunga                                 ]
                    [0. Logout                                      ]
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
                        kumpulan_bunga.append([nama, int(harga), int(stok), warna])
                        print(f"Bunga {nama} udah ditambahin!")
                        input("Tekan enter buat lanjut...")                   
                    elif pilihan == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- Daftar Bunga di Rafalia ---")
                        if not kumpulan_bunga:
                            print("Masih kosong nih, belum ada bunga...")
                        else:
                            for i, bunga in enumerate(kumpulan_bunga, 1):
                                print(f"\n{i}. {bunga[0]}")
                                print(f"   Harga: Rp {bunga[1]:,}")
                                print(f"   Stok: {bunga[2]}")
                                print(f"   Warna: {bunga[3]}")
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- Edit Data Bunga ---")
                        if not kumpulan_bunga:
                            print("Belum ada bunga yang bisa diedit...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        for i in range(len(kumpulan_bunga)):
                            print(f"{i+1}. {kumpulan_bunga[i][0]}")
                        
                        nomor = input("Mau edit bunga nomor berapa? ")
                        if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(kumpulan_bunga):
                            print("Nomor tidak valid atau bukan angka!")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        bunga = int(nomor) - 1
                        print(f"\nEdit data: {kumpulan_bunga[bunga][0]}")
                        
                        nama_baru = input(f"Nama baru [{kumpulan_bunga[bunga][0]}]: ") or kumpulan_bunga[bunga][0]
                        harga_baru = input(f"Harga baru [Rp {kumpulan_bunga[bunga][1]}]: ")
                        stok_baru = input(f"Stok baru [{kumpulan_bunga[bunga][2]}]: ")
                        warna_baru = input(f"Warna baru [{kumpulan_bunga[bunga][3]}]: ") or kumpulan_bunga[bunga][3]
                        
                        kumpulan_bunga[bunga][0] = nama_baru
                        if harga_baru:
                            if harga_baru.isdigit():
                                kumpulan_bunga[bunga][1] = int(harga_baru)
                            else:
                                print("Harga harus angka, data harga nggak berubah")
                        if stok_baru:
                            if stok_baru.isdigit():
                                kumpulan_bunga[bunga][2] = int(stok_baru)
                            else:
                                print("Stok harus angka, data stok nggak berubah")
                        kumpulan_bunga[bunga][3] = warna_baru
                        
                        print("Data berhasil diupdate!")
                        input("Tekan enter buat lanjut...")
                    
                    elif pilihan == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- Hapus Bunga ---")
                        if not kumpulan_bunga:
                            print("Belum ada bunga yang bisa dihapus...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        for i in range(len(kumpulan_bunga)):
                            print(f"{i+1}. {kumpulan_bunga[i][0]}")
                        
                        nomor = input("Mau hapus bunga nomor berapa? ")
                        if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(kumpulan_bunga):
                            print("Nomor tidak valid atau bukan angka!")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        nama_bunga = kumpulan_bunga[int(nomor)-1][0]
                        konfirmasi = input(f"Yakin mau hapus {nama_bunga}? (y/n): ").lower()
                        
                        if konfirmasi == 'y':
                            kumpulan_bunga.pop(int(nomor)-1)
                            print(f"Bunga {nama_bunga} udah dihapus!")
                        else:
                            print("Penghapusan dibatalkan") 
                        input("Tekan enter buat lanjut...")
                    elif pilihan == "0":
                        print("Sampai jumpa lagi!")
                        return True
                    
                    else:
                        print("Pilihan nggak valid, coba lagi...")
                        input("Tekan enter buat lanjut...")
            
            else: 
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
                    ==================================================
                    [    TOKO BUNGA HIAS RAFALIA - PELANGGAN             ]
                    ==================================================
                    [1. Lihat Katalog Bunga                         ]
                    [2. Cari Bunga Favorit                          ]
                    [3. Beli Bunga                                  ]
                    [0. Keluar                                      ]
                    ===================================================
                    """)              
                    pilihan = input("Mau apa? (0-3): ")               
                    if pilihan == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- Katalog Bunga Rafalia ---")
                        if not kumpulan_bunga:
                            print("Maaf, lagi kosong nih...")
                        else:
                            print("Ini bunga-bunga yang ada:")
                            for i, bunga in enumerate(kumpulan_bunga, 1):
                                print(f"\n{i}. {bunga[0]}")
                                print(f"   Harga: Rp {bunga[1]:,}")
                                print(f"   Stok: {bunga[2]}")
                                print(f"   Warna: {bunga[3]}")
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- Cari Bunga ---")
                        if not kumpulan_bunga:
                            print("Belum ada bunga nih...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        keyword = input("Cari bunga apa? ").lower()
                        hasil_cari = []
                        
                        for bunga in kumpulan_bunga:
                            if keyword in bunga[0].lower():
                                hasil_cari.append(bunga)
                        
                        if hasil_cari:
                            print(f"\nDitemukan {len(hasil_cari)} bunga:")
                            for bunga in hasil_cari:
                                print(f"- {bunga[0]} (Rp {bunga[1]:,}) - Stok: {bunga[2]}")
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
                        
                        ada_stok = False
                        for i, bunga in enumerate(kumpulan_bunga):
                            if bunga[2] > 0:
                                if not ada_stok:
                                    print("Bunga yang tersedia:")
                                    ada_stok = True
                                print(f"{i+1}. {bunga[0]} - Rp {bunga[1]:,} (Stok: {bunga[2]})")
                        
                        if not ada_stok:
                            print("Maaf, semua bunga habis...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        pilih = input("\nMau beli yang mana? (masukkan nomor): ")
                        if not pilih.isdigit() or int(pilih) < 1 or int(pilih) > len(kumpulan_bunga):
                            print("Nomor tidak valid atau bukan angka!")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        bunga = int(pilih) - 1
                        bunga_dipilih = kumpulan_bunga[bunga]
                        
                        if bunga_dipilih[2] == 0:
                            print("Stok bunga ini habis!")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        jumlah = input(f"Mau beli berapa {bunga_dipilih[0]}? ")
                        if not jumlah.isdigit() or int(jumlah) <= 0:
                            print("Jumlah harus angka dan lebih dari 0!")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        jumlah = int(jumlah)
                        if jumlah > bunga_dipilih[2]:
                            print(f"Stok tidak cukup! Cuma ada {bunga_dipilih[2]}")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        total = bunga_dipilih[1] * jumlah
                        kumpulan_bunga[bunga][2] -= jumlah
                        
                        print(f"\n Pembelian berhasil! ")
                        print(f"Bunga  : {bunga_dipilih[0]}")
                        print(f"Jumlah : {jumlah}")
                        print(f"Total  : Rp {total:,}")
                        print("Terima kasih udah belanja di Rafalia!")
                        
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "0":
                        print("Makasih udah mampir! Sampai jumpa lagi ")
                        return True
                    
                    else:
                        print("Pilihan nggak valid...")
                        input("Tekan enter buat lanjut...")
            return True  
        
        else:
            print("Login gagal. nama atau password salah.")
            percobaan_login += 1
            if percobaan_login < 3:
                print(f"Kesempatan mencoba tinggal {3 - percobaan_login} lagi")
            input("Tekan enter buat coba lagi...")

    if percobaan_login == 3:
        print("Terlalu banyak percobaan login. Coba lagi nanti ya!")
        input("Tekan enter buat lanjut...")
    return False

# Menu utama
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
     =======================================================
     |                MENU UTAMA RAFALIA                  |
     =======================================================
     | [1] Register (Daftar Akun Baru)                    |
     | [2] Login (Masuk ke Akun)                          |
     | [0] Keluar                                         |
     =======================================================
    """)
    
    pilihan = input("Pilih menu (0-2): ")
    
    if pilihan == "1":
        register()
    elif pilihan == "2":
        login()
    elif pilihan == "0":
        print("Terima kasih telah mengunjungi Toko Bunga Hias Rafalia!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 0-2.")
        input("Tekan enter buat lanjut...")