peso=70.5
estatura=1.71 
imc= peso/(estatura**2)
print("mi imc es de:{imc}\n")
print("mi imc es de: ", {.5,},".format(imc),""\n")
#02 datos de tipo cadena de caracteres 
asignatura="Programacion"
carrera="Ingenieria civil en informatica"
print("La asignatura de ",{asignatura}," coresponde a la carrera de", {carrera})
#3 valores boleanos 
ampolleta= False 
interruptor= True 
print("####### valores boleanes #######")
print(ampolleta,interruptor) 
print(bool(0))
print(bool("**"))
print(bool("none"))
print(bool("true"))
print(bool(1))
print(bool("\n"))
# Listas 
otra_lista=[] #las listas utilizan []
print(type(otra_lista))
estudiantes = ["matias", "marco", "cristobal", "sebastian", "marco"]
num = [1,2,3,4,5,6,]
lenguaje = ["Python"]
listamixta = [1, "felipe", True]
print("lista de cadena de caracteres:", estudiantes)
print("lista de numeros:",num)
print("esta es una lista mixta:",listamixta)
print(len(listamixta)) 
print(estudiantes.count("matias"))
print(estudiantes[0]) 
print(list(num))
print(list(estudiantes))
#05-tuplas-(no mutables)
newtupla=tuple()
grupo1=("daniel","felipe","diego","daniel")
print(type(grupo1))#las tuplas utilizan ()
print("el elemento se repite",grupo1.count("daniel"))
#Muestra el indice del primer elemento
print("el indice del elemento:",grupo1.index ("daniel"))
#Reasignando valor
# grupo1[0]="constanza"
#las tuplas son datos inmutables por lo cual no se puede reasignar el valor
#obteniendo el trozo de una tupla
grupo2=("pedro", 100, "felipe","diego")
print("trozo de la tupla",grupo2[0:3])
#se puede cambiar una tupla a una lista y viseversa
grupo1=list(grupo1)
print("la tupla ahora es del tipo:",type(grupo1),"\n")
#06 - SETS (conjuntos) - estructura fija 
conjunto_vacio= set()                      #los sets utilizan {}
conjunto_vacio1= {}                        #las {} tambien sirven para los diccionarios  
conjunto_animales=({"gato","perro","loro"})#se puede ulilizar asi 
conjunto_colores={"rojo","verde","azul"}   # o asi
#print(conjunto_animales[0])no existe pociciones en SETS
conjunto_colores.add("celeste")            #agregar elemento
print("el conjunto de colores es", conjunto_colores)
#07 Dicionario 
datos_personales={ 
    "nombre":"Felipe",
    "institucion":"Ulagos",
    "edad":29, 
    "asignatura":{"estructura de datos","programacion"}
    }     #se puede tener un set dentreo de un diccionario
datos_personales["institucion"]="USS"

