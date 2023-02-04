#Belajar buat items
#items adalah data dictionary atau list berupa tupple

customer = {"Nama" : "Fajar", "Umur" : 26,"Alamat" : "Bumi Asri"}

Nama = customer ["Nama"]
Umur = customer ["Umur"]
Alamat = customer ["Alamat"]

# for key in customer.items():
#     print (f"{key[0]}:{key[1]}")

#ekstrak 2 variabel
for key, value in customer.items():
    print (f"{key}:{value}")

#cek items print(customer.items())