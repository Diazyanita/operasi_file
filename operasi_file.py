print ("Selamat datang di Program Biodata")
print ("=================================")

# buka file untuk dibaca dan ditulis
baca_bio = open("biodata.txt", "r")
teks = baca_bio.read()

# cetak isi file
print (teks)

# Ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

# format teks
teks = "\nNama: {}\nUmur: {}\nAlamat: {}\n".format(nama, umur, alamat)

# buka file untuk ditulis
file_bio = open("biodata.txt", "a")

# tulis teks ke file
file_bio.write(teks)

# tutup file
file_bio.close()
baca_bio.close()