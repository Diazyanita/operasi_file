print ("Selamat datang di Program Biodata")
print ("=================================")

def baca_file(namafile):
    file = open("biodata.txt", "r")
    print(file.read())
    file.close()

baca_file("biodata.txt")

def tulis_file(nama_file):
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    teks = "\nNama: {}\nUmur: {}\nAlamat: {}\n".format(nama, umur, alamat)
    biodata = open(nama_file, "a")
    print(biodata.write(teks))
    biodata.close()

tulis_file("biodata.txt")