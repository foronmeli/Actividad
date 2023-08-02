import random
cantidad=int(input("Ingrese la cantidad de nuemros de la lista: "))
tamanof=int(input("Digite el en el que finaliza el rango del numero aleatorio: "))
for i in range (1,cantidad+1):
    aleatorio=random.randint(1, tamanof)
    print(aleatorio)
