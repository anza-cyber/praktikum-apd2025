from utils import bersihkan_terminal, tampilkan_tabel_bunga
from data_store import kumpulan_bunga
from promo import tampilkan_promo_hari_ini

def menu_pelanggan():
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
            tampilkan_tabel_bunga(kumpulan_bunga)
            input("Enter...")

        elif pilihan == "2":
            bersihkan_terminal()
            print("--- Cari Bunga Favorit ---")
            if not kumpulan_bunga:
                print("Belum ada bunga nih...")
                input("Enter...")
                continue

            keyword = input("Masukkan nama bunga yang dicari: ").lower()
            hasil_cari = {nama: data for nama, data in kumpulan_bunga.items() if keyword in nama.lower()}

            if hasil_cari:
                print(f"\nDitemukan {len(hasil_cari)} bunga:")
                tampilkan_tabel_bunga(hasil_cari)
            else:
                print("Bunga yang dicari tidak ditemukan.")
            input("Enter...")

        elif pilihan == "3":
            bersihkan_terminal()
            print("--- Beli Bunga ---")
            if not kumpulan_bunga:
                print("Lagi kosong, gak bisa beli...")
                input("Enter...")
                continue

            tampilkan_tabel_bunga(kumpulan_bunga)
            nama_bunga = input("\nMasukkan nama bunga yang ingin dibeli: ")

            if nama_bunga not in kumpulan_bunga:
                print("Bunga tidak ditemukan!")
                input("Enter...")
                continue

            bunga = kumpulan_bunga[nama_bunga]
            print(f"Stok tersedia: {bunga['stok']}")
            try:
                jumlah = int(input("Mau beli berapa: "))
            except ValueError:
                print("Input jumlah harus angka ya...")
                input("Enter...")
                continue

            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                input("Enter...")
                continue

            if jumlah > bunga['stok']:
                print(f"Stok tidak cukup! Tersisa {bunga['stok']} bunga saja.")
                input("Enter...")
                continue

            total_harga = bunga['harga'] * jumlah
            print(f"\nTotal yang harus dibayar: Rp {total_harga:,}")
            konfirmasi = input("Lanjutkan pembelian? (y/n): ").lower()

            if konfirmasi == 'y':
                kumpulan_bunga[nama_bunga]['stok'] -= jumlah
                print(f"\nPembelian berhasil! Kamu membeli {jumlah} {nama_bunga}.")
                print("Terima kasih sudah berbelanja di Toko Bunga Rafalia 💐")
            else:
                print("Pembelian dibatalkan.")
            input("Enter...")

        elif pilihan == "4":
            bersihkan_terminal()
            print("--- Coba Faktorial ---")

            def hitung_faktorial(n):
                return 1 if n <= 1 else n * hitung_faktorial(n - 1)

            try:
                angka = int(input("Masukkan angka untuk dihitung faktorialnya: "))
                if angka < 0:
                    print("Angka tidak boleh negatif!")
                else:
                    hasil = hitung_faktorial(angka)
                    print(f"Hasil dari {angka}! = {hasil}")
            except ValueError:
                print("Input harus berupa angka.")
            input("Enter...")

        elif pilihan == "0":
            print("Makasih udah mampir! Sampai jumpa lagi ya bye bye")
            return
        else:
            print("Pilihan gak valid...")
            input("Enter...")
