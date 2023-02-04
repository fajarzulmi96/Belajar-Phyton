#Belajar method/function

#cara tidak efektif
# nama = []

# nama.append("Fauzi")
# print("========")
# for data in nama :
#     print(data)

# nama.append("Fajar")
# print("========")
# for data in nama :
#    print(data)

# nama.append("Kurniawan")
# print("========")
# for data in nama :
#    print(data)

#menggunakan method
nama = []

def print_nama():
    print("=======")
    for data in nama :
        print(data)

nama.append("Fajar")
print_nama()

nama.append("Fauzi")
print_nama()

nama.append("Kurniawan")
print_nama()
