set1 ={100, 250, 300, 1000}
set2 = {150, 250, 500, 1000}
#A)
if 100 in set1:
    print("100 esta en el primer set")
else:
    print("100 no esta en el primer set") 

if 100 in set2:
    print("100 esta en el segundo set")
else:
    print("100 no esta en el segundo set") 
#B)
if 500 in set1:
    print("500 esta en el primer set")
elif 700 in set1:
    print("700 esta en el primer set")

if 500 in set2:
    print("500 esta en el segundo set")
elif 700 in set2:
    print("700 esta en el segundo set") 
#C)

#D)
list1=list(set1)
list2=list(set2)
set5=list1+list2
set5=set(set5)
print(set5)
print(type(set5))