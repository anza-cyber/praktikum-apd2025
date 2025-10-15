nama = "Rafalia"
nim = "104"
percobaan = 0
total = 0

while percobaan < 3:
    Masukan_nama = input(" Masukan nama anda : ")
    password     = input(" Masukan Password  : ") 

    if Masukan_nama == nama and password == nim:
        print(" Selamat Login Anda Berhasil ")
        Login_Berhasil = "MARI SHOPPING"
        while True:
            print(" === MENU PILIHAN FURNITUR TOKO RAFALIA === ")
            print(" 1. Sofa                      - Rp 500.000  ")
            print(" 2. Meja Belajar               - Rp 250.000 ")
            print(" 3. Rak Lemari                 - Rp 150.000 ")
            print(" 4. Keluar dari program                     ")
            pilihan = input("Silahkan pilih Barang yang anda ingin ")
            if pilihan =="4":
                print("Terima kasih Telah menggunakan layanan ini")
                break


            if pilihan == "1":
                jenis  = "sofa"
                harga  = 500.000
                
            elif pilihan == "2":
                jenis    = "meja belajar"
                harga    = 250.000

            else:
                jenis    = "rak lemari"
                harga    = 150.000
            jumlah_furnitur =int(input(" Masukan Jumlah Barang yang anda mau "))
            confirmasi = input("Apakah anda ingin lanjut shopping ? ")
            if confirmasi == "yes":
                pass  
            elif confirmasi == "no ":     

                for w in range (jumlah_furnitur):
                    total += harga

                    print(" ===  STRUK PEMBELIAN === ")
                    print(" Jenis Barang yang anda beli : ", jenis)
                    print(" Jumlah barang yang anda beli :", jumlah_furnitur)
                    print("Total Harga Yang anda Shopping :",total)
                    print(" ========================================= ")
                break
        break        
            
    else:
        percobaan += 1
        print(" YAHH GAGAL ")
        print(" WOII JANGAN KEBANYAKAN SPAM ",percobaan)
        print(" -------------------- ")









