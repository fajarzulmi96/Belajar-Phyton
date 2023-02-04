import cmath
#1 bilangan real & imaginer bilangan kompleks
# Bilangan kompleks dilambangkan dengan “ x + yi “. Python mengubah bilangan real x dan y 
# menjadi kompleks menggunakan fungsi kompleks(x,y). Bagian real dapat diakses menggunakan 
# fungsi real() dan bagian imajiner dapat direpresentasikan dengan imag().
#Inisialisasi bilangan real
x = 5
y = 3
#mengubah x dan y menjadi bilangan kompleks
z = complex(x,y);
#print bagian real dan imaginer dari bilangan kompleks
print ("bagian bilangan real dari bilangan kompleks : ",end="")
print (z.real)
print ("bagian bilangan imaginer dari bilangan kompleks : ",end="")
print (z.imag)
