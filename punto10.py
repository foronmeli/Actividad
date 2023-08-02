numero=int(input("Digite un numero: "))
factorial=1
if numero==1:
    factorial=1
else:
    for i in range (2,numero+1):
        factorial=factorial*i
print("El factorial del numero es: ",factorial)
