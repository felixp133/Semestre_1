#EJERCICIO N°4
n = int(input("Ingrese el valor que sera elevado al cubo: "))

f = (n * (n - 1)) + 1

if (n / 2) == float :
    r = (n ** 2) + (n + 1)
else :
    r = (n ** 2) + n

nicomaco = list(range(f, r, 2)) 

cubo = sum(nicomaco)

print("El resultado de elevar ", n,"al cubo es: ",cubo)

""""

1 ** 3 = 1
2 ** 3 = 3 + 5
3 ** 3 = 7 + 9 + 11
4 ** 3 = 13 + 15 + 17 + 19
5 ** 3 = 21 + 23 + 25 + 27 + 29

"""