
ciudades= ["santiago","temuco","osorno","punta arenas"]
calidadaire=[134,99,245,50]

auxiliar=(zip(ciudades,calidadaire)) 
auxiliar2=(zip(ciudades,calidadaire)) 

ciudad_mayor=max(auxiliar,key=lambda x : x[1])
ciudad_menor=min(auxiliar2,key=lambda x : x[1])
print("la ciudad con mayor indice de contaminacion es " ,ciudad_mayor[0]," con ",ciudad_mayor[1])
print("la ciudad con menor indice de contaminacion es ", ciudad_menor[0]," con ",ciudad_menor[1] ) 

if ciudad_mayor[1]>300:
    print("la calidad del aire de" , ciudad_mayor[0],  "es peligrosa")
elif 300<=ciudad_mayor[1]>201 : 
    print("la calidad del aire de" , ciudad_mayor[0]," es muy dañina para la salud")
elif 200<=ciudad_mayor[1]>151 :
    print("la calidad del aire de" , ciudad_mayor[0],  "es dañina para la salud")
elif 150<= ciudad_mayor[1]>101:
    print("la calidad del aire de" , ciudad_mayor[0],  "es dañia para la salud de personas sensibles") 
elif 100<=ciudad_mayor[1]>51:
    print("la calidad del aire de" , ciudad_mayor[0],  "es moderada")
else : 
    print("la calidad del aire de" , ciudad_mayor[0],  "es buena")


if ciudad_menor[1]>300:
    print("la calidad del aire de" , ciudad_menor[0],  "es peligrosa")
elif 300<=ciudad_menor[1]>201 : 
    print("la calidad del aire de" , ciudad_menor[0]," es muy dañina para la salud")
elif 200<=ciudad_menor[1]>151 :
    print("la calidad del aire de" , ciudad_menor[0],  "es dañina para la salud")
elif 150<= ciudad_menor[1]>101:
    print("la calidad del aire de" , ciudad_menor[0],  "es dañia para la salud de personas sensibles") 
elif 100<=ciudad_menor[1]>51:
    print("la calidad del aire de" , ciudad_menor[0],  "es moderada")
else : 
    print("la calidad del aire de" , ciudad_menor[0],  "es buena")

