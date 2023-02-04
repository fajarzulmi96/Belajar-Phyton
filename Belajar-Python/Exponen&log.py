#Operasi complex number

# exp() :- Fungsi ini mengembalikan eksponen dari bilangan kompleks yang disebutkan dalam argumennya.
# log(x,b) :- Fungsi ini mengembalikan nilai logaritmik dari x dengan basis b, keduanya disebutkan dalam 
# --> argumennya. Jika basis tidak ditentukan, log natural dari x dikembalikan.
# Python code to demonstrate the working of
# exp(), log()

# import cmath untuk operasi matematika
import cmath
import math

# Inisialisasi bilangan real
x = 1.0
y = 1.0

# konversi x dan y ke bilangan kompleks
z = complex(x, y);

# print exponent
print ("exponent dari bilangan kompleks adalah : ", end="")
print (cmath.exp(z))

# print log
print ("log dari bilangan kompleks adalah  : ", end="")
print (cmath.log(z,10))
