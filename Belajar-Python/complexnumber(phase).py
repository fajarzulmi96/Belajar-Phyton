import cmath
#2 fase bilangan kompleks
# Secara geometris, fase bilangan kompleks adalah sudut antara sumbu real positif dan vektor yang 
# mewakili bilangan kompleks. Ini juga dikenal sebagai argumen bilangan kompleks. Fase dikembalikan
# menggunakan fase(), yang menggunakan bilangan kompleks sebagai argumen. Kisaran fase terletak dari 
# -pi hingga +pi. yaitu dari -3,14 hingga +3,14

#Inisialisasi bilangan real
x = -1.0
y = 0.0

#mengubah x dan y menjadi bilangan kompleks
z = complex(x,y);

# print bilangan kompleks dengan phase ()
print ("fase bilangan kompleks adalah : ",end="")
print (cmath.phase(z))
 
