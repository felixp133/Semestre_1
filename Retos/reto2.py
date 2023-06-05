
notas={}
nombre=input("escriba su nombre: ")
asignatura=input("escriba la asignatura: ")
Lab1=float(input("Su nota 1 es: "))
Lab2=float(input("Su nota 2 es: "))
promedio=float(Lab1*0.3+Lab2*0.7)
notas={ 
    "nombre":nombre,
    "asignatura":asignatura , 
    "Lab1":Lab1,
    "Lab2":Lab2,
    "Promedio":promedio 
    }
print(notas)


