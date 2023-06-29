superficie8=23890
personas8=1556805
superficie10=48583
personas10=828708
#A)
region8={
    "Region":"Bio Bio",
    "Superficie":superficie8,
    "Habitantes":personas8,
}
region10={ 
    "Region":"Los lagos",
    "Superficie":superficie10,
    "Habitantes":personas10,
} 
print(region8) 
print(region10)
#B)
Densidad8=(personas8/superficie8)
Densidad10=(personas10/superficie10)
region8["Densidad"]=round(Densidad8)
region10["Densidad"]=round(Densidad10) 
print(region8)
print(region10) 
#C)
region8["Capital"]="Consepcion"
region10["Capital"]="Puerto Montt"
print(region8)
print(region10)
#D)
region8["Provincias"]=["Biobío","Arauco","Concepción"]
region10["Provincias"]=["Osorno", "Llanquihue","Chiloé", "Palena"]
#E) y F)
region8["Comunas"]=("Lota", "Lebu", "Los Ángeles")
region10["Comunas"]=("Castro", "Puerto Varas", "Purranque")
print(region8)
print(region10) 
