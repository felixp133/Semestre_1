nombre=input("Escriba su nombre: ")
direccion=input("Escriba su direccion: ")
ciudad=input("Escriba su ciudad: ")
numero=input("Escriba su numero de telefono: ")

diccionario={
    "Nombre": nombre,
    "Direccion": direccion,
    "Ciudad": ciudad,
    "Numero telefonico":numero,   
}
print(diccionario)
Facebook=input("agregue su facebook: ")
twiter=input("agregue su twitter: ")
instagram=input("agregue su instagram: ")
diccionario["Redes sociales"] = Facebook , twiter, instagram
print("El facebook es: ", Facebook)
print(diccionario) 
