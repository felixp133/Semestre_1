#01 Numero mayor y Menor de una lista
n1= float(input("ingrse el primer numero "))
n2= float(input("ingrse el segundo numero "))
n3= float(input("ingrse el tercer numero ")) 
if n2<n1>n3: 
    print("El numero mayor es ",n1)
elif n1<n2>n3:
    print("El numero mayor es ",n2)
elif n1<n3>n2:
    print("El numero mayor es ",n3)
else : 
    print("Todos los numeros son iguales")
print("######################################################################################")
#02
V1=input("ingrese la primera palabra: ")
V2=input("ingrese la seguna palabra: ")
if len(V1)>len(V2):
    print("La palabra ", V1," tiene mas caracteres")
else: 
    print("La palabra ", V2," tiene mas caracteres")

print("#####################################################################################")
#03 Triangulos 
 #indica si el triangulo es equilatero, isoseceles o escaleno 
print("A continuacion escriba los lados del triangulo")
l1= float(input("Escriba el primer lado ")) 
l2= float(input("Esciba el segundo lado "))
l3= float(input("Escriba el tercer lado ")) 
p=(l1+l2+l3) / 2
Area= p*(p-l1)*(p-l2)*(p-l3)
if l1==l2==l3:
    print("El triangulo es equilatero")
elif l1!=l2 and  l2 != l3: 
    print("El triangulo es escaleno")
else:
    print("El triangulo es isoceles")     
print("El su area del triangulo es: ", Area) 
print("######################################################################################")
#04 

print("######################################################################################")
#05 Promedio Ponderado 
n1=float(input("Ingrese la primera nota: "))
n2=float(input("Ingrese la segunda nota: "))
n3=float(input("Ingrese la terecera nota: "))
promedio=  n1*0.3 + n2*0.4 + n3*0.3 
if promedio < 4.0:
    print("Usted reprobo la asignatura")
elif promedio > 4.0 and promedio < 6.0 :
    print("Usted aprobo la asignatura")
elif promedio > 6.0: 
    print("Usted aprobo con distincion la asignatura") 
print("######################################################################################") 

