#for loop + dictionary

customer = {"Nama" : "Fajar", "Umur" : 26,"Alamat" : "Bumi Asri"}

Nama = customer ["Nama"]
Umur = customer ["Umur"]
Alamat = customer ["Alamat"]

for key in customer:
    value = customer[key]
    print (f"{key}:{value}")