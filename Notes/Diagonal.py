from random import randrange
N=int(input("Dame la dimension de la matriz: "))
#matriz = [[(randrange(1,11)) for j in range(N)] for i in range(N)]
matriz =[]
for f in range(N):
    matriz.append([])
    for c in range(N):
        matriz[f].append(randrange(1,11))
print(matriz)
suma1=0
suma2=0
for f in range(N):
    suma1+=matriz[f][f]
    suma2+=matriz[f][N-1-f]
print("La suma de la diagonal de arriba hacia abajo es: ",suma1)
print("La suma de la diagonal de arriba hacia abajo es: ",suma2)