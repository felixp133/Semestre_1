
Lista_a = ["Rojo", "Verde", "Celeste", "Violeta"]
Lista_b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]

#A) Crear una función para encontrar la palabra que tiene más caracteres de la lista a
print("Palabra con más caracteres de la lista a:")

def encontrar_palabra_mas_larga(lista_a):
    palabra_mas_larga = lista_a[0]
    for palabra in lista_a:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

resultado_a = encontrar_palabra_mas_larga(Lista_a)
print(resultado_a)

#B) Crear una función para encontrar la palabra que tiene menos caracteres de la lista b
print(".")
print("Palabra con menos caracteres de la lista b:")

def encontrar_palabra_mas_corta(lista_b):
    palabra_mas_corta = lista_b[0]
    for palabra in lista_b:
        if len(palabra) < len(palabra_mas_corta):
            palabra_mas_corta = palabra
    return palabra_mas_corta

resultado_b = encontrar_palabra_mas_corta(Lista_b)
print(resultado_b)

#C) Crear una función que concatene ambas listas
print(".")
print("Listas concatenadas:")

def concatenar_listas(lista_a, lista_b):
    lista_concatenada = lista_a + lista_b
    return lista_concatenada

resultado = concatenar_listas(Lista_a, Lista_b)
print(resultado)

#D) Crea una función que transforme los elementos de la lista en Mayúsculas.
print(".")
print("Lista concatenada con elementos en mayúsculas:")

def convertir_a_mayusculas(lista):
    lista_mayusculas = [palabra.upper() for palabra in lista]
    return lista_mayusculas

resultado_d = convertir_a_mayusculas(Lista_a + Lista_b)
print(resultado_d)

#E) Crear una función y ordenar la lista de forma alfabética.
print(".")
print("Lista ordenada de forma alfabética:")

def ordenar_lista(resultado_d):
    lista_ordenada = sorted(resultado_d)
    return lista_ordenada

resultado_e = ordenar_lista(resultado_d)
print(resultado_e)
