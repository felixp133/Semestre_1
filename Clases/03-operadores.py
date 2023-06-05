a=2
b=3 
print("suma entre a y b: ", a + b)
print("resta entre a y b: ", a - b)
print("multiplicasion entre a y b: ", a * b)
print("division entre a y b; ", a / b )
print("cociente entre a y b: ", a // b)
print("modulo de a y b: ", a % b)
c2=complex(3, -5)
print("hola" * 5 ) 
#02 operadores de comparaciom 
print("igual", a==b )
print("desigual ",a != b)
print(" mayor ", a>b)
print("menor ", a<b )
print("mayor igual ", a>=b)
print("menor igual ", a<=b)
#03 operadores logicos
# o=or 
# y=and 
#no=not = cambia el valor al contrario
bencina= True
ensendido=True 
edad=19 
if bencina and ensendido:
    print("el veiculo puede avanzar")
else: 
    print("el veiculo no puede avanzar")

if bencina or ensendido: 
    print("el veiculo puede arrancar")
else: 
    print("el veiculo no puede avanzar") 

if not bencina and ensendido: 
    print("el veiculo puee avanzar") 
else: 
    print("el veiculo no puede avazar") 

if not bencina or (ensendido and edad >= 18):
    print("el veiculo puede avanzar ")
else:
    print("el veiculo no puede avanzar ")
#Operadores ternario 
