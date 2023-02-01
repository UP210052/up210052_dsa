from random import randrange
lista=[0,0,0,0,0]
i=0
while i<5:
    igual=False
    a=randrange(1,11)
    for l in range(5):
        if (lista[l]==a):
            igual=True
    if igual == False:
        lista[i]=a
        i+=1
print(lista)