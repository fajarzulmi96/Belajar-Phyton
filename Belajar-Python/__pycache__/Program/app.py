#Program manajemen kontak
import function
#list of dictionary
daftar_kontak = []
daftar_kontak.append({
    "Nama" : "Fajar Zulmi Sopian",
    "Email" : "fajarsopian220@gmail.com",
    "Telpon" : "082123848572"
})
#Menu program
while True:
    print("#Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("0 keluar program")

    menu = input("Pilih Menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        daftar_kontak.append (function.new_kontak())


print("Program selesai dijalankan sampai jumpa")
