from random import randrange

def imprimir(matriz3,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            print(matriz3[f][c], end=" ")
        print()

filas=int(input("Dame las filas: "))
columnas=int(input("Dame las columnas:"))
matriz = [[randrange(1,11) for j in range(columnas)] for i in range(filas)]
matriz2=[]

for f in range(columnas):
    matriz2.append([])
    for c in range(filas):
        matriz2[f].append(matriz[c][f])
print("Matriz normal: ")
imprimir(matriz,filas,columnas)
print("-----------------")
print("Matriz transpuesta: ")
imprimir(matriz2,columnas,filas)