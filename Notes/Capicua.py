numero=input("Dame un numero:")
lista=list(numero)
igual=0
for i in range(len(lista)):
    if  lista[i]==lista[(len(lista))-i-1]:
        igual+=1
if igual == int(len(lista)):
    print ("El numero es Capicua")
else:
    print ("El numero no es Capicua")