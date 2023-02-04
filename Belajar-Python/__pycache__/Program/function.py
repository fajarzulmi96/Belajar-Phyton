#Program manajemen kontak

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print ("============")
        print (f"Nama : {kontak ['Nama']}")
        print (f"Email : {kontak ['Email']}")
        print (f"Telpon : {kontak ['Telpon']}")

def new_kontak():
    Nama = input("Input Nama :")
    Email = input("Input Email :")
    Telpon = input("Input Telpon")
    Kontak = {
        "Nama" : Nama,
        "Email" : Email,
        "Telpon" : Telpon 
    }
    return Kontak

def 
