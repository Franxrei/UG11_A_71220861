kata1 = input("Masukkan kata : ")
def Huruf(str):
    strLength = len(str)
    if strLength % 2 == 0 :
        return str[0] + str[1] + str[2] + ' dan ' + str[-3] + str[-2] + str[-1]
    else :
        tengah = int(strLength / 2)
        return str[tengah - 1] + str[tengah] + str[tengah+1]


find = Huruf(kata1)
print("Huruf yang diambil pada kata ", kata1," adalah",find)