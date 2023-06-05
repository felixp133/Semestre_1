#EJERCICIO N°3
Tdiurno = 12000
Tnocturno = 16000

domD= Tdiurno+2000
domN= Tnocturno+3000

print("Pago diario empleado 1")
emp1={
    "Lunes":Tnocturno*10,
    "Martes":Tnocturno*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Viernes":Tdiurno*10,
}
print(emp1)
print(" ")

print("Pago diario empleado 2")
emp2={
    "Martes":Tnocturno*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Domingo":domD*10,
}
print(emp2)
print(" ")

print("Pago diario empleado 3")
emp3={
    "Sabado":Tnocturno*10,
    "Domingo":domN*10,
    "Miercoles":Tnocturno*10,
    "Jueves":Tdiurno*10,
    "Viernes":Tdiurno*10,
}
print(emp3)
print(" ")

tsemanal1=sum(emp1.values())
tsemanal2=sum(emp2.values())
tsemanal3=sum(emp3.values())

tsemanal={
    'Empleado 1':tsemanal1,
    'Empleado 2':tsemanal2,
    'Empleado 3':tsemanal3,
}

print("Ls tarifas semanales son: \n")
print(tsemanal)
print(" ")