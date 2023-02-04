#Trigonometri

# sin() : Fungsi ini mengembalikan sinus dari bilangan kompleks yang diteruskan dalam argumen.
# cos() : This function returns the cosine of the complex number passed in argument.
# tan() : Fungsi ini mengembalikan tangen dari bilangan kompleks yang diteruskan dalam argumen.

# Python code to demonstrate the working of
# sin(), cos(), tan()

import cmath

x = 1.0

y = 1.0

z = complex(x,y);

# printt sin
print ("Value sin adalah : ",end="")
print (cmath.sin(z))

# print cos
print ("value cos adalah : ",end="")
print (cmath.cos(z))

# print tan
print ("value tan adalah : ",end="")
print (cmath.tan(z))
