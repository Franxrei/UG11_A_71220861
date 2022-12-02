print("================= Program Manipulasi String ===================")
print("=                        Pilihan Menu :                       =")
print("=                       1.Hitung kata                         =")
print("=                        2.Ubah Kata                          =")
pilihan = input("=                       Pilihan Anda  : ")
kalimat = input("=                 Masukan Sebuah kalimat/kata : ")


def hitung():
    satu=input("=               Masukan kata yang ingin dihitung : ")
    satusatu =kalimat.count(satu)
    print("=        Terdapat sebanyak ",satusatu," kata ",satu," di dalam kalimat")

def ubah():
    dua= input("=           Masukan kata yang ingin diubah : ")
    duadua= input("=           Masukan kata pengganti : ")
    tiga=kalimat.replace(dua, duadua)
    print("=             String berhasil diubah menjadi :",tiga)


if pilihan=="1":
    hitung()
elif pilihan=="2":
    ubah()
else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")