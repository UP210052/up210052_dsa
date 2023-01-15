print("Hola mundo")
print ("Hola mundo"*2)

entero = 7 // 2 # Es la parte entera de la divicion
residuo = 7 % 2 
potencia = 2 ** 3
raiz = 16 **.5

print(entero)
print(residuo)
print(potencia)
print(raiz)

print(-4 - -4) #unario signo de un numero

print(9 % 6 % 2) #izquierda a derecha
print(2 ** 2 ** 3) #derecha a izquierda

keywords = ['False', 'None','True','True']
print(keywords[-1])
print(keywords.index('True'))
keywords.pop #quita el ultimo
print(keywords)
keywords.insert(2, "Juan")
print(keywords)
print(keywords.count('True'))
#pilas quitas el ultimo
#colas quitas el primero
#listas quitas cualquiera

print(round(3.14159,2)) #round para redondear

def ordenar(stack):          #Crear funciones 
    return len(stack) == 0

print("-----------------------------------------")

a= [5,2,7,9,3]
for i in range(0, len(a)): #Estructura for
   print (a[i])

print("-----------------------------------------")

# Bubble sort
for i in range(0, len(a)+1 -2):
    for j in range(0, len(a)+1 -i-2):
        x=a[j]
        y=a[j+1]
        if x > y: #Estructura de if
            a[j]=y
            a[j+1]=x

print(a)

def doble(num):
    y = num * 2
    return y

print(doble(10))

b=10
if b>10:
    print("El valor de B es mayor a 10")
else:
    print("El valor de B es menor o igula a 10")

print("-----------------------------------------")

print("Pitagoras")
cateto_A=3
cateto_B=4

def pitagoras(A,B):
    C=( A*A + B*B) ** 0.5
    return C

print(pitagoras(cateto_A, cateto_B))

print("-----------------------------------------")

import os
import time

print("Cual es tu apellido: ")
lastName=input()
name=input("Cual es tu nombre: ")
edad = int(input("Cual es tu edad: "))
print(type(edad)) #tipo

completoName= name + " " + lastName #concatenar
print("Hi ", completoName)

os.system("cls") #Limpiar pantalla
time.sleep(2) #Pausar lo de imprimir