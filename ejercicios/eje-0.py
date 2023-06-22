variable=[1,4]            #Lista
variable2=2.4457
variable3="hola mundo"    
variable4=set(1,7,4,6,9)  #Set
variable5=(4,5,6,7,8,9)   #Tupla
####################################TIPOS DE DATOS############################################################
float()            #todos los numeros tienen un decimal
int()              #contene los valores en enteros
bool()             #combierte los valores en booleanos (TRUE o FALSE)
complex()          #combierte los numeros a numeros complejos
str()              #combierte en cadena de texto
type()             #dice el tipo de dato que es una variable          
#####################################FUNCIONES################################################################
variable.append(2) #agregar elemento en la ultima posicion
variable.insert(2,3)#insertar elemento en una posicion 
variable.remove(2,3)#quitar elemento
variable.pop       #quita el ultimo elemnto 
variable3.lower    #combierte las mayusculas en minuculas
variable.count     #cuenta las veces que se repite un elemento
variable3.split    #separa los elementos dee una frase
variable.extend    #combina 2 o mas listas
variable.index     # 
variable.sort      #ordena de forma desendente
#variable4.        #
len(variable3)     #le la cantidad de caracteres de una palabra
round(variable)    #redondea el resultado de una operacion
sum(variable)      #suma los elemntos de una variable, lista , sets o tublas
max(variable)      #toma el caracter de mayor valor
min(variable)      #toma el caracter de menor valor
print("{:.2f}".format(variable2)) #esto sirve para delimitar decimales
print(round(variable2,1))#Redondea a una cantidad de decimales
####################FUNCIONES IMPORTADAS####################################################################
from time import sleep
sleep()     #Imprime cada x segundo
from math import factorial
factorial() # multiplica los numeros menores a el numero elejido
