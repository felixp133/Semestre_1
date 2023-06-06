 
def leerfrase ():
    frase=input(str("Ingrese una frase: "))
    separacion=frase.split()
        
    diccionario={}

    for i in separacion:
        diccionario[i]=len(i)

    print(diccionario)

leerfrase()