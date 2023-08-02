texto=str(input("Digite una palabra: "))
V=[]
V2=[]
for i in texto:
    V.append(i)
print(V)
for i in range (len(V)-1,-1,-1):
    valor=V[i]
    V2.append(valor)
print(V2)
if V==V2:
    print("La palabra SI es polindroma")
else:
    print("La palabra NO es polindroma")
