import random

secretNumber=random.randint(0,30)
win=False
while win==False:
    num=int(input("Dame un numero: "))
    if num<secretNumber:
        print("Subele")
    elif num>secretNumber:
        print("Bajale")
    elif num==secretNumber:
        print("Bingo ganaste")
        win=True
#subele, bajale, bingo y conteo