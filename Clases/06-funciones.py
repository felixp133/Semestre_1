#01-Declarando la primera Funcion
def mi_primera_funcion (): 
    print("Esta es mi primera funcion")

mi_primera_funcion #si escribes el nombre de la funcion, lanza el print 
                   #esto se puede hacer con listas, bucles, etc
#02-Declarando y funcion y una lista

def concatenar(lista1,lista2):
    return lista1+lista2

lista1=[1,2,3]
lista2=[3,4,5]
print(concatenar(lista1,lista2));

#03-Declarando una funcion y multiplicacion
def multiplicacion (num1,num2):
    return num1*num2

print(multiplicacion(10,2)) #aqui se le da un valor a num1 y num2 pero sin crear una variable

#Ejemplo de una funcion suma y resta por teclado 

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b 
a=int(input("Ingrse el valor de a: "))
b=int(input("Ingrse el valor de b: "))
#se llama a la funcion suma 
resultado=suma(a,b)
print("El resultado de la suma entre ",a," y ", b ," es ", resultado)
#se llama a la funcion resta
resultado2=resta(a,b)
print("El resultado de la resta entre ",a," y ", b ," es ", resultado2)
