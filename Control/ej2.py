lista1=[10,9,12,15,18] 
lista2=[21,8,15,3,12] 

print("la lista 1 es: ",lista1)
print("la lista 2 es: ",lista2) 
#A)
lista3=lista1+lista2 
print("juntaremos ambas listas ")
print(" la nueva lista es: ", lista3)
#B)
lista3.insert(1, 30)
print(" al agregar el numero 30 en la posision 2 nos da lo siguiente: ", lista3) 
#C)

#D)
lista4=[4,5,6]
lista5=lista3+lista4
print(lista5)
#E)
print("la suma de toda la lista es: ", sum(lista5))
#F) 
media=(sum(lista5)/len(lista5))
print("la media de la lista es: ", media)
print("la mediana de la lista es: ", lista5[6])
