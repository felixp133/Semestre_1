frase=input(str("Ingrese una frase: "))
def funcion1 ():

    quitar=",.;:\n!\""
    for caracter in quitar:           
        frase=frase.replace(caracter,
                    "")   
    
    frase=frase.lower()
    palabras=frase.split() 
    v1=frase.count
    lfrase=len(frase)
    diccionario={
        "cantidad de palabras ":v1,
        "Longitud de frase":lfrase ,

    }
    print(diccionario)


print(funcion1)