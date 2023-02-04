#Belajar argumen list
#jika ingin menambahkan argumen list didepannya
#argumen list tidak bisa dua
#Cara tidak efektif
# def jumlahkan (satu, dua, tiga=0, empat=0):
#    total = satu + dua + tiga + empat
#    print (f"Total {[satu, dua, tiga, empat]} = {total}")

# jumlahkan (10, 10 )


#Menggunakan list argumen
def jumlahkan (*list_angka):
    total = 0
    for angka in list_angka :
        total = total + angka
    print (f"Total {list_angka} = {total}")

jumlahkan(10,10,10)