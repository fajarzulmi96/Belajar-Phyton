# #Operasi complex number

# isfinite() :- Mengembalikan true jika bagian nyata dan imajiner dari bilangan kompleks 
# -->> berhingga, jika tidak mengembalikan false.
# isinf() :- Mengembalikan true jika bagian nyata atau imajiner dari bilangan kompleks
# -->> adalah/tidak terbatas, jika tidak mengembalikan false.
# isnan() :- Mengembalikan true jika bagian nyata atau imajiner dari bilangan kompleks
# -->> adalah NaN , jika tidak mengembalikan false.
# Kode python untuk mendemonstrasikan cara kerja
# isnan(), isinf(), isfinite()

# importing "cmath" for complex number operations
import cmath
import math

x = 1.0
y = 1.0
a = math.inf
b = math.nan

z = complex(x,y);

w = complex(x,a);

v = complex(x,b);

# cek apakah kedua angka itu terbatas
if cmath.isfinite(z):
	print ("Bilangan kompleks terbatas")
else : print ("Bilangan kompleks tidak terbatas")
	
# cek  apakah salah satu nomor tidak terbatas
if cmath.isinf(w):
	print ("Bilangan kompleks tidak terbatas")
else : print ("Bilangan kompleks terbatase")

# cek apakah salah satu nomor tidak terbatas
if cmath.isnan(v):
	print ("Bilangan Kompleks NaN")
else : print ("Bilangan Kompleks tidak NaN")
