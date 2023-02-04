#Hyperbolic

# sinh() : Fungsi ini mengembalikan sinus hiperbolik dari bilangan kompleks yang diteruskan 
# -->> dalam argumen.
# cosh() : Fungsi ini mengembalikan kosinus hiperbolik dari bilangan kompleks yang diteruskan
# -->> dalam argumen.
# tanh() : Fungsi ini mengembalikan tangen hiperbolik dari bilangan kompleks yang diteruskan 
# -->> dalam argumen.

# Python code to demonstrate the working of
# sinh(), cosh(), tanh()

import cmath

x = 1.0

y = 1.0

z = complex(x,y);

# print hyperbolic sin
print ("value hyperbolic sin adalah : ",end="")
print (cmath.sinh(z))

# print hyperbolic cos
print ("value hyperbolic cos adalah : ",end="")
print (cmath.cosh(z))

# print hyperbolic tan
print ("value hyperbolic tan adalah : ",end="")
print (cmath.tanh(z))
