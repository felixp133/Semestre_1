'''
Realizar un programa donde el usuario indique la cantidad de números que va a ingresar,
luego solicitar dicha cantidad de números e imprimir en pantalla, la suma de todos es-
tos números, la suma de los pares y la suma de los impares. Se debe resolver utilizando
funciones para cada una de las operaciones mencionadas anteriormente.
'''

#El usuario indica la cantidad de números a ingresar y luego se solicita su ingreso:

números_ingresados  = []
print("Indique la cantidad de números que desea ingresar: ")
A_ingresar = int(input())

numeros = A_ingresar

for x in range(numeros):
    print("Ingrese su número: ")
    NUMs = int(input())
    números_ingresados.append(NUMs)

#Se imprimen los números ingresados:

print("Los números ingresados son: ", números_ingresados)

#Se suman los números ingresados:

sumados = sum(números_ingresados)
print("El resultado al sumar los números: ", sumados)

#Se suman los pares e impares:

suma_pares = 0
suma_impares = 0
    
for i in números_ingresados:
    if i % 2 == 0:
     suma_pares = suma_pares + i
    else:
     suma_impares = suma_impares + i

print("La cantidad al sumar solo los números pares: ", suma_pares)
print("La cantidad al sumar solo los números impares: ", suma_impares)




