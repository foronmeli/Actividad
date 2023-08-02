mayor=-9999999999999999999999999999999999999999999999999999999999999999999999999
menor=99999999999999999999999999999999999999999999999999999999999999999999999999
lista=[3,5,1,5,2]
for i in range (0,len(lista)):
    if lista[i]>mayor:
        mayor=lista[i]
    elif lista[i]<menor:
        menor=lista[i]
print("El mayor es: ",mayor," y el menor es: ",menor)
