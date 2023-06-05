#Bucles 
edad=15
num=0
#Bucles infinitos  
#while edad < 18 : 
#    print("eres menor de edad") 
#while True: 
#  #   print(num)
#  num +=2  Esto es para sumar de 2 en 2 a un numero, en este caso a 0, infinitamente
#Bucles normales 
while num <= 100 :
    print(num)
    num +=2 
print("El primer bucle termino")

while num <= 200 : 
    print(num)
    num +=2 
else: 
    print("Mi condicion es igual o mayor a 200")
print("El segundo bucle se termino")
while num <= 300: 
    print(num)
    num +=2
    if num==250: 
        print("mi condicion es igual a 250")
print("El tercer bucle se termino")

while num <=400 :
    print(num)
    num +=2
    if num == 350: 
        print("Se detiene la ejecucion")
        break
print(num)
print("El cuarto bucle se termino")
#Loop infinito 
#while True:
 #   parametro= input(">")
  #  if parametro == "exit":
   #     break
    #else: 
     #   print(parametro) 
#impresion de una lista de 10 elemento en forma vertical utilizando for
# FOR N°1 
for i in (1,2,3,4,5,6,7,8,9,10):  #esto no esta bien hecho
    print(i)
#FOR N°2
newlist=[1,2,3,4,5,6,7,8,9,10]
for i in newlist:               #esto si esta bien hecho 
    print(i)
# FOR N°3 
for i in range(11):    #el RANGE empieza a contar desde el 0 por eso se pone 11 
    print(i)
 
for i in range(1,11):  #con esto sacamos el 0  
    print(i)