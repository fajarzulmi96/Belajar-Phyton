#Belajar return value
#Ada dua jenis method yang pertama hanya mengeksekusi kode program
#method function method yang mengembalikan nilai

def jumlahkan (*list_angka):
    total = 0
    for angka in list_angka :
        total = total + angka
    return total#mengembalikan nilai total dan memasukan ke variabel

total = jumlahkan(10, 10, 10)
print(total)
