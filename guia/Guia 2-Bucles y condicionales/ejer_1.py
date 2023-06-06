texto= """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica""" 

quitar=",.;:\n!\""
for caracter in quitar:           #quitamos los puntos y comas 
    texto=texto.replace(caracter,
                    "")   
texto=texto.lower()               #combierte las letras mayusculas a minusculas       
v1=texto.count("universidad")
palabras=texto.split()
tupla1=tuple(palabras)     

print("la palabra universidad se repite",v1,"veces") 
#print(tupla2)    
print(tupla1) 
print(type(tupla1)) 

#En la guia no espesificaba si la tupla tenia que tener todas las palabras o solo las 3 veces que se 
#repite universidad, asi que hice que la tupla tubiera todas las palabras del texto .