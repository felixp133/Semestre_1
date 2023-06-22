from time import sleep

def bisiesto():
    añob=list(range(0,2024))  
    for año in añob:
        if año % 4 == 0 and (año % 100 !=0 or año % 400 == 0):
            sleep(1)
            print(f"El año {año} es Bisiesto ")
        else:
            sleep(1)
            print(f"El año {año} no es Bisiesto")   

bisiesto()
