'''Desarrollar un programa que permita al usuario ingresar una serie de numeros enteros 
positivos (N numeros) hasta que ingrese -1 (Solo positivos ignorando los numeros negativos).
Luego, el programa debe calcular e imprimir en pantalla lo siguiente: el numero 
mayor de los ingresados, la sumatoria total de los numeros, la sumatoria de los numeros 
pares, la sumatoria de los numeros impares y el promedio total. Ademas, se debe imprimir 
si el numero mayor obtenido es mayor, menor o igual que el promedio calculado. 
Asegurate de resolver este problema utilizando las funciones que consideres adecuadas.
Nota: el -1 no se cuenta. Si el usuario ingresa un numero negativo debe volver a pedir un 
numero y no se usa en el calculo.'''

print("Ingrese los numeros que desee (Solo positivos)")
print("Para cerrar el ciclo ingrese -1")
x = 0
datos = []

while x!= -1:
        x = int(input(">"))
        datos.append(x)

print(datos)

datos.remove(-1)

#Suma de pares
#Suma de impares
par = 0
impar = 0

for i in datos:
        if i % 2 == 0:
                par = par + i
        else:
                impar = impar + i
print("La suma de los numeros pares es:", par)
print("La suma de los numeros impares es:", impar)

#Suma total
sum_total = sum(datos)
print("La suma total es:", sum_total)

#Promedio
promedio = round(sum(datos)/len(datos),2)
print("El promedio es:", promedio)

#N° mayor ingresado
mayor= max(datos)
print("El numero mayor es:", mayor)

#si el numero mayor obtenido es mayor, menor o igual que el promedio calculado.
if mayor > promedio:
        print("EL numero mayor es", mayor, "y es mayor al promedio")
elif mayor == promedio:
        print("El numero mayor es", mayor, "y es igual al promedio")
else:
        print("EL numero mayor es", mayor, "y es menor al promedio")




