
# github.com/carlosherrerah/Matricula_dsa
'''
horas = int(input("Dame las horas: "))
minutos = int(input("Dame los minutos: "))
duracion = int(input("Dame la duracion: "))
horasFinal= (horas + ((minutos+duracion) // 60)) % 24
minutosFinal= (minutos+duracion) % 60
print (horasFinal,":",minutosFinal)
'''
print("---------------------------------------")
#round para redondear
A=0
B=0
C=0
if A>B and A>C:
    print(A)
elif B>A and B>C:
    print(B)
elif C>A and C>B:
    print(C)

if A>=B:
    if A>=C:
        print(A)
    elif C>A:
        print(C)
elif B>=A:
    if C>B:
        print(C)
    elif B>=C:
        print(B)

print("---------------------------------------")

#Redondear
print(round(.1515521,3))
print("%.3f" % .1515521)
print(f'{.1515521:.3f}')
print(f'{100000:,.2f}')
print(f'{123:0<6d}')
#La multiplicacion prece a la suma 
# 20.12E8

print("---------------------------------------")

# up210052_dsa
# U1 - O1Biseccion.py
n=int(input("Numero: "))
print(n>=100)

s=(2,1,6) #tupla
d=[7,8,9] #list