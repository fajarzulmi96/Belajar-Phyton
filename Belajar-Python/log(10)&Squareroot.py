#Operasi complex number

# log10() :- Fungsi ini mengembalikan basis log 10 dari bilangan kompleks.
# sqrt() :- Ini menghitung akar kuadrat dari bilangan kompleks.

import cmath
import math

x = 1.0
y = 1.0

z = complex(x, y);

# print log10 
print ("The log10 of complex number is : ", end="")
print (cmath.log10(z))

# print square rootr
print ("The square root of complex number is : ", end="")
print (cmath.sqrt(z))
