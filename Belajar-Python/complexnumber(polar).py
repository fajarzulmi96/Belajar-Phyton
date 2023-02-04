import cmath
#3 Konversi ke polar dilakukan dengan menggunakan polar(), yang mengembalikan pasangan(r,ph) yang 
# menunjukkan modulus r dan sudut fase ph. modulus dapat ditampilkan menggunakan abs() dan 
# fase menggunakan fase().Bilangan kompleks diubah menjadi koordinat persegi panjang dengan 
# menggunakan rect(r, ph), di mana r adalah modulus dan ph adalah sudut fasa. Ini mengembalikan 
# nilai secara numerik sama dengan r * (math.cos(ph) + math.sin(ph)*1j)

# Python code to demonstrate the working of
# polar() and rect()

# Inisialisasi bilangan real
x = 1.0
y = 1.0

# Mengubah x dan y menjadi bilangan kompleks
z = complex(x,y);

# konvwesi bilangan kompleks ke polar dengan polar()
w = cmath.polar(z)

# print modulus dan dan argumen di bilangan kompleks polar
print ("The modulus and argument of polar complex number is : ",end="")
print (w)

# konversi bilangan kompleks ke rectangular menggunakan rectt()
w = cmath.rect(1.4142135623730951, 0.7853981633974483)

# print form rectangular dari bilangan kompleks
print ("The rectangular form of complex number is : ",end="")
print (w)
