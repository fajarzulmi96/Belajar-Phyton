#Trigonometri

# asin() : Fungsi ini mengembalikan sinus busur dari bilangan kompleks yang diteruskan dalam argumen
# acos() : Fungsi ini mengembalikan arc cosinus dari bilangan kompleks yang diteruskan dalam argumen.
# atan() : Fungsi ini mengembalikan tangen busur dari bilangan kompleks yang diteruskan dalam argumen.

# Python code to demonstrate the working of
# asin(), acos(), atan()


import cmath

x = 1.0

y = 1.0

z = complex(x,y);

# printing arc sin
print ("arc sin adalah: ",end="")
print (cmath.asin(z))

# printing arc cos
print ("arc cos adalah : ",end="")
print (cmath.acos(z))

# printing arc tan
print ("arc tan adalah : ",end="")
print (cmath.atan(z))
