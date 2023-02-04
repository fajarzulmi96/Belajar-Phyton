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

for i in range (0, len(nama)) :
    data_nama = nama[i]
    data_umur = umur[i]
    data_alamat = alamat[i]
    data_asal_sekolah = asal_sekolah [i]
    data_bagian = bagian [i]

print(f"{data_nama} berumur {data_umur} tinggal {data_alamat} dari sekolah {data_asal_sekolah} bekerja di bagian {data_bagian}")

