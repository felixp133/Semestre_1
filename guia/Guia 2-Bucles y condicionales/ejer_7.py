#EJERCICIO N°7
from math import factorial

n = int(input("Ingrese su valor: "))

if n == 0 :
    print(1)
else :
    factor = n * factorial(n - 1)
    print(factor)