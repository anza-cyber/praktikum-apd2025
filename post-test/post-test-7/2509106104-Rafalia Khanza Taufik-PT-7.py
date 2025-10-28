import os

print("""
     =======================================================
     |      Selamat Datang di Toko Bunga Hias Rafalia      |
     =======================================================
    """)

data_pengguna = {}
kumpulan_bunga = {}
total_transaksi_hari_ini = 0
jumlah_pengunjung = 0
diskon_member = 0.05

def hitung_diskon(total_belanja, status_member):
    if status_member and total_belanja > 50000:
        potongan = total_belanja * diskon_member
        return potongan
    return 0

def tampilkan_info_bunga(nama, harga, stok):
    print(f"Nama : {nama}")
    print(f"Harga: Rp {harga:,}")
    print(f"Stok : {stok}")

def hitung_total_pembelian():
    """Fungsi tanpa parameter untuk hitung total"""
    total = 0
    for bunga in kumpulan_bunga.values():
        total += bunga["harga"] * 10
    return total

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

def tampilkan_promo_hari_ini():
    print("\n PROMO CUMAN HARI INI")
    print("Diskon 5% untuk member setia")
    print("Pembelian di atas Rp 50.000 gratis kartu ucapan")
    print("Point rewardnya bisa ditukar hadiah loh...")

def bersihkan_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def hitung_faktorial(angka):
    """Fungsi rekursif untuk hitung faktorial"""
    if angka == 1 or angka == 0:
        return 1
    elif angka < 0:
        return "Gak bisa hitung faktorial dong kalo angka negatif"
    else:
        return angka * hitung_faktorial(angka - 1)

def cek_input_angka(teks_input):
    while True:
        nilai = input(teks_input)
        if nilai == "":
            return 0
        if nilai.isdigit():
            return int(nilai)
        else:
            print("Harus angka bulat dong! Coba lagi.")

def cek_angka_biasa(teks):
    nilai = input(teks)
    if nilai == "":
        return None
    if nilai.isdigit():
        return int(nilai)
    else:
        return "invalid"

def validasi_stok(nama_bunga, jumlah):
    if nama_bunga not in kumpulan_bunga:
        print(f"Bunga {nama_bunga} gak ada di daftar menu bunga")
        return False
    
    stok_sekarang = kumpulan_bunga[nama_bunga]["stok"]
    if jumlah > stok_sekarang:
        print(f"Maaf ya, stok bunganya cuman {stok_sekarang}")
        return False
    
    return True

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
            jenis_akun = "admin" if role == "admin" else "pelanggan"
            waktu_dibuat = "sekarang"
            status_akun = "aktif"
            point_awal = 100 if role == "pelanggan" else 0
            
            print(pesan_berhasil)
            if role == "pelanggan":
                print(f"Kamu dapat {point_awal} point")
            input("Tekan enter buat lanjut...")
            break

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
                        bersihkan_terminal()
                        print("--- Tambah Bunga Baru ---")
                        nama_bunga = input("Nama bunga: ")
                        harga = cek_input_angka("Harganya: Rp ")
                        stok = cek_input_angka("Stok tersedia: ")
                        warna = input("Warna: ")
                        
                        if harga <= 0 or stok < 0:
                            print("Harga harus lebih dari 0 ya! dan stok gak boleh negatif!")
                            input("Tekan enter buat lanjut...")
                            continue
                                      
                        kumpulan_bunga[nama_bunga] = {
                            "harga": harga,
                            "stok": stok,
                            "warna": warna
                        }
                        print(f"Bunga {nama_bunga} udah ditambahin!")
                        input("Tekan enter buat lanjut...")                   
                    elif pilihan == "2":
                        bersihkan_terminal()
                        print("--- Daftar Bunga di Toko Rafalia ---")
                        if not kumpulan_bunga:
                            print("Masih kosong nih, belum ada bunga...")
                        else:
                            nomor = 1
                            for nama_bunga, data in kumpulan_bunga.items():
                                print(f"\n{nomor}. {nama_bunga}")
                                print(f"   Harga: Rp {data['harga']:,}")
                                print(f"   Stok: {data['stok']}")
                                print(f"   Warna: {data['warna']}")
                                nomor += 1
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "3":
                        bersihkan_terminal()
                        print("--- Edit Data Bunga ---")
                        if not kumpulan_bunga:
                            print("Belum ada bunga yang bisa diedit...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        nomor = 1
                        for nama_bunga in kumpulan_bunga.keys():
                            print(f"{nomor}. {nama_bunga}")
                            nomor += 1
                        
                        nama_edit = input("Masukkan nama bunga yang mau diedit: ")
                        if nama_edit not in kumpulan_bunga:
                            print("Bunga gak ditemukan!")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        bunga = kumpulan_bunga[nama_edit]
                        print(f"\nEdit data: {nama_edit}")
                        
                        nama_baru = input(f"Nama baru [{nama_edit}]: ") or nama_edit
                        harga_input = cek_angka_biasa(f"Harga baru [Rp {bunga['harga']}]: ")
                        stok_input = cek_angka_biasa(f"Stok baru [{bunga['stok']}]: ")
                        warna_baru = input(f"Warna baru [{bunga['warna']}]: ") or bunga['warna']
                        
                        if nama_baru != nama_edit:
                            kumpulan_bunga[nama_baru] = kumpulan_bunga.pop(nama_edit)
                            bunga = kumpulan_bunga[nama_baru]
                        
                        if harga_input is not None:
                            if harga_input != "invalid":
                                bunga["harga"] = harga_input
                            else:
                                print("Harga harus angka, data harga gak berubah")
                        if stok_input is not None:
                            if stok_input != "invalid":
                                bunga["stok"] = stok_input
                            else:
                                print("Stok harus angka, data stok gak berubah")
                        bunga["warna"] = warna_baru
                        
                        print("Data berhasil diupdate!")
                        input("Tekan enter buat lanjut...")
                    
                    elif pilihan == "4":
                        bersihkan_terminal()
                        print("--- Hapus Bunga ---")
                        if not kumpulan_bunga:
                            print("Belum ada bunga yang bisa dihapus...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        nomor = 1
                        for nama_bunga in kumpulan_bunga.keys():
                            print(f"{nomor}. {nama_bunga}")
                            nomor += 1
                        
                        nama_hapus = input("Masukkan nama bunga yang mau dihapus: ")
                        if nama_hapus not in kumpulan_bunga:
                            print("Bunga gak ditemukan!")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        konfirmasi = input(f"Yakin mau hapus {nama_hapus}? (y/n): ")
                        if konfirmasi == 'y' or konfirmasi == 'Y':
                            del kumpulan_bunga[nama_hapus]
                            print(f"Bunga {nama_hapus} udah dihapus!")
                        else:
                            print("Penghapusan dibatalkan") 
                        input("Tekan enter buat lanjut...")
                    
                    elif pilihan == "5":
                        bersihkan_terminal()
                        print("=== INFO TOKO RAFALIA ===")
                        tampilkan_jumlah_pengguna()
                        total_nilai = hitung_total_pembelian()
                        print(f"Total nilai stok: Rp {total_nilai:,}")
                        print(f"Pengunjung hari ini: {jumlah_pengunjung}")
                        print(f"\nBonus: 5! = {hitung_faktorial(5)}")
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "0":
                        print("Sampai jumpa lagi ya!")
                        return True
                    
                    else:
                        print("Pilihan gak valid, coba lagi...")
                        input("Tekan enter buat lanjut...")
            
            else: 
                while True:
                    bersihkan_terminal()
                    print(f"""
                    ==================================================
                    [    TOKO BUNGA HIAS RAFALIA - PELANGGAN         ]
                    ==================================================
                    [1. Lihat Menu Bunga                            ]
                    [2. Cari Bunga Favorit                          ]
                    [3. Beli Bunga                                  ]
                    [4. Coba Faktorial                              ]
                    [0. Logout                                      ]
                    ===================================================
                    """)              
                    pilihan = input("Mau apa? (0-4): ")               
                    if pilihan == "1":
                        bersihkan_terminal()
                        print("--- Menu Bunga Rafalia ---")
                        if not kumpulan_bunga:
                            print("Maaf, lagi kosong nih...")
                        else:
                            print("Ini bunga-bunga yang ada:")
                            nomor = 1
                            for nama_bunga, data in kumpulan_bunga.items():
                                print(f"\n{nomor}. {nama_bunga}")
                                print(f"   Harga: Rp {data['harga']:,}")
                                print(f"   Stok: {data['stok']}")
                                print(f"   Warna: {data['warna']}")
                                nomor += 1
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "2":
                        bersihkan_terminal()
                        print("--- Cari Bunga ---")
                        if not kumpulan_bunga:
                            print("Belum ada bunga nih...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        kata_kunci = input("Cari bunga apa? ")
                        bunga_ditemukan = {}
                        
                        for nama_bunga, data in kumpulan_bunga.items():
                            if kata_kunci in nama_bunga:
                                bunga_ditemukan[nama_bunga] = data       
                        if bunga_ditemukan:
                            print(f"\nDitemukan {len(bunga_ditemukan)} bunga:")
                            nomor = 1
                            for nama_bunga, data in bunga_ditemukan.items():
                                print(f"{nomor}. {nama_bunga} (Rp {data['harga']:,}) - Stok: {data['stok']}")
                                nomor += 1
                        else:
                            print("Bunga yang dicari lagi kosong nih...")
                        
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "3":
                        bersihkan_terminal()
                        print("--- Beli Bunga ---")
                        if not kumpulan_bunga:
                            print("Lagi kosong, gak bisa beli...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        ada_stok = False
                        print("Bunga yang tersedia:")
                        nomor = 1
                        for nama_bunga, data in kumpulan_bunga.items():
                            if data['stok'] > 0:
                                ada_stok = True
                                print(f"{nomor}. {nama_bunga} - Rp {data['harga']:,} (Stok: {data['stok']})")
                            nomor += 1
                        if not ada_stok:
                            print("Maaf, semua bunga habis...")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        nama_beli = input("\nMau beli bunga apa? (masukkan nama): ")      
                        if not validasi_stok(nama_beli, 1):
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        bunga_dipilih = kumpulan_bunga[nama_beli]
                        jumlah = cek_input_angka(f"Mau beli berapa {nama_beli}? ")    
                        if jumlah <= 0:
                            print("Jumlah harus lebih dari 0!")
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        if not validasi_stok(nama_beli, jumlah):
                            input("Tekan enter buat lanjut...")
                            continue
                        
                        subtotal = bunga_dipilih['harga'] * jumlah
                        potongan = hitung_diskon(subtotal, True)
                        total_bayar = subtotal - potongan
     
                        kumpulan_bunga[nama_beli]['stok'] -= jumlah
                        global total_transaksi_hari_ini
                        total_transaksi_hari_ini += total_bayar   
                        print(f"\nPembelian berhasil! ")
                        tampilkan_info_bunga(nama_beli, bunga_dipilih['harga'], jumlah)
                        if potongan > 0:
                            print(f"Diskon : Rp {potongan:,}")
                        print(f"Total  : Rp {total_bayar:,}")
                        print("Terima kasih udah belanja di Toko Bunga Rafalia!")  
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "4":
                        bersihkan_terminal()
                        print("--- Coba Hitung Faktorial ---")
                        angka = cek_input_angka("Masukkan angka: ")
                        if angka < 0:
                            print("Gak bisa hitung faktorial kalo angka negatif")
                        else:
                            hasil = hitung_faktorial(angka)
                            print(f"Hasil {angka}! = {hasil}")
                        input("\nTekan enter buat lanjut...")
                    
                    elif pilihan == "0":
                        print("Makasih udah mampir! Sampai jumpa lagi ya bye bye ")
                        return True
                    
                    else:
                        print("Pilihan gak valid nih...")
                        input("Tekan enter buat lanjut...")
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