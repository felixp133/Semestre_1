#Condicionales
licencia= False
edad=19 
auto= False 

if licencia == True :
    print()

 
#CONDICIONAL IF

licencia = False
edad = 19
automovil = False

if licencia:
    print("Puedo conducir porque tengo licencia")
else:
    print("No tengo licencia para conducir")


if licencia:
    print("Puedo conducir porque tengo licencia\n")
else:
    print("No tengo licencia para conducir\n")
print("Este print esta fuera del else")


if edad:
    print("Puedo conducir porque soy mayor de edad\n")
else:
    print("No puedo conducir soy menor de edad\n")
    
if edad >= 18:
    print("Puedo conducir porque soy mayor de edad\n")
else:
    print("No puedo conducir soy menor de edad\n")


if licencia and edad >= 18:
    print("Puedo conducir porque soy mayor de edad y tengo licencia")
elif automovil:
    print("Tengo automovil, pero no tengo licencia ni la edad necesaria")
else:
    print("No puedo conducir no tengo ni la edad, ni licencia ni automovil")

