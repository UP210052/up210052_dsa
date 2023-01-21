for i in range(3):
    pass
    # continue regresa al inicio del ciclo
    print(i)
    # break
print("Fin")
user_word = input("Dame una palabra: ")
user_word = user_word.upper()
new_word = ""
for letter in user_word:
    if letter not in ("A","E","I","O","U"):
        new_word+=letter
print(new_word)

c0=1000
paso=0
while c0!=1:
    if c0 % 2 == 0:
        c0=c0/2
    else:
        c0= c0 * 3 + 1
    paso+=1
    print(c0)
print("Pasos:", paso)
# para quitar el salto de linea es end=""
# and conjuction ^
# or disjunction v
'''
operaciones con bits 
$ conjuction
| disjunction
~ negacion
^ xor 

len longitud0
'''
# .remove() quita el primero que encuentra
# del elimina por pocision
# .pop() quita el ultimo elemnto y lo muestra
# .append() ingresa al final
# .insert() ingrasa un valor en el lugar indicado
# .sort() ordena el vector
# len longitud del vector
# replace() remplaza una palabra con lo indicado
# split() divide el vector en dos cuando hay un espacio 
# np.sum() suma los datos de los vectores


# c:\> pip install numpy
# import numpy as np libreria matematica de numeros

# landa 

numeros=[10,5,6,7,8,9]
numeros.sort()
print(numeros)
