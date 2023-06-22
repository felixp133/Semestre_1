'''
Diseñar un algoritmo que pueda actuar como un cajero, que devuelve y desglosa el vuelto
en billetes y monedas (pesos chilenos). Utilizando funciones en Python.
'''
import json

#Se muestra una serie de productos:

print("Productos deportivos disponibles: ")

diccionario = {
              "Balon de futbol": 15990,
              "Zapatos de futbol Adidas": 99990,
              "Zapatos de futbol Nike": 105000,
              "Espinilleras": 12990,
              "Guantes de portero": 45990
              }

print(json.dumps(diccionario, sort_keys=False, indent=4))

#Se pide ingresar el valor del producto elegido:

print("Ingrese el valor del producto a comprar:")
compra = int(input("CLP "))

#Se pide ingresar la cantidad monetaria con la que se pagara el producto:

print("Ingrese la cantidad con la que se pagara:")
pago = int(input("CLP "))

while pago < 0:
    print("Ingrese una cantidad valida por favor:")
    pago = int(input("CLP "))

#Se realiza el calculo del vuelto:

def resta(compra,pago):
    return pago-compra

resultado = resta(compra,pago)

print("Su vuelto es de: CLP", resultado)

#Se lleva a cabo el desglose de la cantidad en billetes y monedas:

veintemil = resultado // 20000
resultado = resultado % 20000
print(veintemil, "Billete/s de 20.000")
diezmil = resultado // 10000
resultado = resultado % 10000
print(diezmil, "Billete/s de 10.000")
cincomil = resultado // 5000
resultado = resultado % 5000
print(cincomil, "Billete/s de 5.000")
mil = resultado // 1000
resultado = resultado % 1000
print(mil, "Billete/s de 1.000")
quinientos = resultado // 500
resultado = resultado % 500
print(quinientos, "moneda/s de 500")
cien = resultado // 100
resultado = resultado % 100
print(cien, "moneda/s de 100")
cincuenta = resultado // 50
resultado = resultado % 50
print(cincuenta, "moneda/s de 50")
diez = resultado // 10
resultado = resultado % 10
print(diez, "moneda/s de 10")

