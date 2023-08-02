M=[]
filas=int(input("Digite la cantidad de filas: "))
columnas=int(input("Digite la cantidad de columnas: "))
for i in range(0,filas):
    fila=[]
    for j in range(0,columnas):
        numero = int(input("Digite un numero para la fila: "))
        fila.append(numero)
        M.append(fila)
print(M)
