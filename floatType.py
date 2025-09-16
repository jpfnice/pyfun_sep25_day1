
"""
float: real numbers
     + - * / // % **
"""

nb= 12.34 # "fixed" notation
print(nb, type(nb))

nb=12. # "fixed" notation
print(nb, type(nb))

nb=.78 # "fixed" notation
print(nb, type(nb))

nb= -5.47E+12 # "scientific" notation
print(nb, type(nb))

nb=float()
print(nb)

nb=float(234)
print(nb)

nb=float("567.7")
print(nb)

print(45677.3E+256 ** 3) # OverflowError