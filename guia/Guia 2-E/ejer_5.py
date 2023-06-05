#EJERCICIO N°5
import random
n=random.sample(range(40,350),20)

print(n)
print(" ")

nSEARCH=int(input("Que numero desea buscar?\n"))

ocurrN= n.count(nSEARCH)

print(f"El numero {nSEARCH} tiene {ocurrN} numero de ocurrencias")