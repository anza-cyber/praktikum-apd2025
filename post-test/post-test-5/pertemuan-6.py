# listNama = ["dapupu", "bambang", "ucup", "otong"]

#print(listNama[1])

# # Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9} 
# for angka in angka_ganjil: 
#     print(angka)

# angka_ganjil.discard(11)
# print(angka_ganjil)

# Daftar_buku = { 
#     "Buku1" : "Bumi Manusia", 
#     "Buku2" : "Laut Bercerita",
#     "Buku3" : "Anak Semua Bangsa" 
# }

# print(Daftar_buku["Buku2"])
# print(Daftar_buku)

# for rafa in Daftar_buku :
#     print(rafa)

# for values in Daftar_buku.values():
#     print(values)

# for rafa in Daftar_buku.items():
#     print(rafa)

# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "Jaringan Komputer, "Sistem Operasi"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {"Instagram" : "daffahrhap"}
#     }

# #print(Biodata["Nama"])
# print(Biodata["KRS"][1:5:2])

# list nama = dict(mahasiswa1= "Dapupu", 
#                  mahasiswa2="Bambang", 
#                  mahasiswa3="Ucup", 
#                  mahasiswa4="Otong")

# print(f"nama saya adalah {Biodata["Nama"]}") 
# print(f"Instagram : {Biodata['Social Media']['Instagram']}") 
# print(f"nama saya adalah {Biodata.get("Nama")}") 
# print(Biodata.get("Nama"))

# Film = { 
#     "Avenger Endgame" : "Action", 
#     "Sherlock Holmes" : "Mystery", 
#     "The Conjuring" : "Horror"
# }
#Sebelum Ditambah 
#print(Film)

# Film["Zombieland"] = "Comedy" 
# Film.update({"Hours" : "Thriller"})
#Setelah Ditambah 
#print(Film)

#Sebelum Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
#'The Conjuring': 'Horror'}

#Setelah Ditambah 
#{'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
#'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours': 'Thriller'}

# print(Film)
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 'The Conjuring': 'Horror'}
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Action', 'The Conjuring': 'Tragedy'}

# data = { 
#     "Nama" : "Daffa", 
#     "Umur" : 19, 
#     "Jurusan" : "Informatika" } 
#Sebelum Dihapus 
#print(data) 
# del data["Nama"] 
# #Setelah diubah

# data = { 
#     "Nama" : "Daffa", 
#     "Umur" : 19, 
#     "Jurusan" : "Informatika" 
#     } 
#Sebelum Dihapus 
# print(data) 
# data.clear() 
# #Setelah dihapus 
# print(data) 
#{'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
# {}

# buku = { 
#     "Buku1" : "Bumi Manusia", "Buku2" : "Laut Bercerita" 
# } 
# pinjam = buku.copy() 

# print("Dictionary yang telah disalin : ", pinjam) 

# Dictionary yang telah disalin : {"Buku1" : "Bumi Manusia", "Buku2" : "Laut Bercerita"}

# key = "apel", "jeruk", "mangga" 
# value = 1 
# buah = dict.fromkeys(key, value) 
# print(buah) 

# Musik = {
#      "The Chainsmoker" : ["All we Know", "The Paris"], 
#      "Alan Walker" : ["Alone", "Lily"], 
#      "Neffex" : ["Best of Me", "Memories"] 
#      } 
# for i, j in Musik.items(): 
#     print(f"Musik milik {i} adalah : ") 
#     for song in j: 
#         print(song)
#     print("") 
    