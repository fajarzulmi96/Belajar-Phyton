#Hyperbolic
# asinh() : Fungsi ini mengembalikan sinus hiperbolik terbalik dari bilangan kompleks 
# -->> yang diteruskan dalam argumen.
# acosh() : Fungsi ini mengembalikan kosinus hiperbolik terbalik dari bilangan kompleks
# -->> yang diteruskan dalam argumen.
# atanh() : Fungsi ini mengembalikan tangen hiperbolik terbalik dari bilangan kompleks 
# -->> yang diteruskan dalam argumen.

# Python code to demonstrate the working of
# asinh(), acosh(), atanh()

import cmath

x = 1.0

y = 1.0

z = complex(x,y);

# print inverse hyperbolic sin
print ("value inverse hyperbolic sin adalah : ",end="")
print (cmath.asinh(z))

# print inverse hyperbolic cosin
print ("value inverse hyperbolic sin adalah: ",end="")
print (cmath.acosh(z))

# print inverse hyperbolic tan
print ("value inverse hyperbolic tan adalah : ",end="")
print (cmath.atanh(z))
