#return value dengan tupple

def jumlahkan (*list_angka):
    total = 0
    for angka in list_angka :
        total = total + angka
    return (list_angka, total)#menggunakan tupple untuk mengembalikan nilai 2 angka

list_angka, total = jumlahkan(10, 10, 10)
print(f"Total {list_angka} = {total}")