pacientes = [ ["Pedro", 1.78], ["Constanza", 1.56], ["Amanda", 1.62] , ["Dario", 1.89],
["Fernanda", 1.67] ]
#A)
def estatura_minima(pacientes):
    estmin=min(pacientes) 
    print(estmin)
estatura_minima
#print(estatura_minima)
#B)
Npaciente=["Ricardo",[1.71]]
def nuevo_pciente (pacientes):
    pacientes2=pacientes+Npaciente
    return pacientes2 
print (nuevo_pciente)
    
#C)
def encuentra_dario(pacientes2):
    for i in pacientes2 :
        if i in "Dario":
            print("El paciente dario si se encentra en la lista")
            print(pacientes2[3])
        else:
            print("El paciente dario no se encentra en la lista")

#D)
estatura_minima(pacientes)
nuevo_pciente(pacientes)
encuentra_dario(pacientes)
