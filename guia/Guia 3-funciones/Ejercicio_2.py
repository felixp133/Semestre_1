def solisitud_nombres():
    nombres=[]
    print("escriba 'termino' para que deje de pedir datos")
    while True:
        n=str(input("ingrese un nombre: "))
        if n == "termino":
            break
        nombres.append(n)
    return nombres

nombre=solisitud_nombres()

def letra(nombres):
    letras=0
    for i in nombres:
        letras += len(i)
    return letras 

letras=letra(nombre)

def total(nombres,letras):
    for i in nombres:
        print(i)
    print("el total de letras de los nombres ingresados es: ",letras)

total(nombre,letras)


