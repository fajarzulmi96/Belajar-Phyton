#Membuat program menggunakan for loop, list dan range

banyak = int (input("Berapa banyak data ?"))

nama = []
umur = []
alamat = []
asal_sekolah = []
bagian = []

for i in range (0, banyak) :
    print (f"Data ke {i}" )
    input_nama = input("nama :")
    input_umur = int(input("umur :"))
    input_alamat = input("alamat :")
    input_asal_sekolah = input("Asal Sekolah :")
    input_bagian = input("Bagian :")

    nama.append(input_nama)
    umur.append(input_umur)
    alamat.append(input_alamat)
    asal_sekolah.append(input_asal_sekolah)
    bagian.append(input_bagian)

print(nama)
print(umur)
print(alamat)
print(asal_sekolah)
print(bagian)