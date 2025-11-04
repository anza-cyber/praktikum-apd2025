from prettytable import PrettyTable

def tampilkan_promo_hari_ini():
    print("\n PROMO CUMAN HARI INI")
    print("Diskon 5% untuk member setia")
    print("Pembelian di atas Rp 50.000 gratis kartu ucapan")
    print("Point rewardnya bisa ditukar hadiah loh...")

    table = PrettyTable()
    table.field_names = ["Jenis Promo", "Keterangan"]
    table.add_row(["Diskon", "5% untuk member setia"])
    table.add_row(["Bonus", "Gratis kartu ucapan untuk belanja > Rp50.000"])
    table.add_row(["Reward", "Point bisa ditukar hadiah"])
    print(table)
