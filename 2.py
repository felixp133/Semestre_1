'''
Utilizar una funcion que permita ingresar nombres para que el usuario ingrese nombres 
uno por uno. Los nombres se deben almacenar en una lista. Luego, crear otra funcion
que permita contar las letras, la cual debe recorrer la lista de nombres y cuente la 
cantidad total de letras de todos los nombres ingresados. Por ultimo, crear una funcion para 
que imprima los resultados y muestre en pantalla los nombres ingresados y el total de
letras contadas.
'''
             
def ingreso():
    nombres=[]
    while True:
        nombre=input("nombre>> ")
        if nombre == "exit":
            break
        nombres.append(nombre)
    return nombres

def letras(nombres):
    total_letras=0
    for nombre in nombres:
        total_letras+= len(nombre)
    return total_letras

def resultado(nombres,letras ):
    for nombre in nombres:
        print(nombre)
    print(letras)

nombres = ingreso()
total_letras = letras(nombres)
resultado(nombres, total_letras)

'''
def ingresar_nombres():
    nombres = []
    while True:
        nombre = input("Ingresa un nombre (o escribe 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        nombres.append(nombre)
    return nombres

def contar_letras(nombres):
    total_letras = 0
    for nombre in nombres:
        total_letras += len(nombre)
    return total_letras

def imprimir_resultados(nombres, total_letras):
    print("Nombres ingresados:")
    for nombre in nombres:
        print(nombre)
    print("Total de letras contadas:", total_letras)

# Ejemplo de uso
nombres = ingresar_nombres()
total_letras = contar_letras(nombres)
imprimir_resultados(nombres, total_letras)
'''