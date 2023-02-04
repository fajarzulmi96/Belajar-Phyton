#Belajar tipe data dictionary
#bisa mengganti indeks dari integer menjadi string

customer = {"Nama" : "Fajar", "Umur" : 26,"Alamat" : "Bumi Asri"}
#Nama = Key
#Fajar = Value

#Cara manual
# Nama = customer ["Nama"]
# Umur = customer ["Umur"]
# Alamat = customer ["Alamat"]
# print(Nama)
# print(Umur)
# print(Alamat)
# print(Company)

#menambah dictionary
customer["Company"] = "PT Prima Makmur Rotokemindo"
#mengubah dictionary
customer["Nama"] = "Fauzi"
#menghapus data pada dictionary
del customer["Alamat"]

for key, value in customer.items():
    print (f"{key}:{value}")

