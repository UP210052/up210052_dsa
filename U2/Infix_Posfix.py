def prioridad(simbolo):
        if simbolo in ['+','-']:
                return 1
        elif simbolo in ['*','/']:
                return 2
        elif simbolo == '^':
                return 3
        elif simbolo in ['(']:
                return 4
        else:
               return 0
infix = '5 * ( 6 + 2 ) - 12 / 4'
posfix = '5 6 2 + * 12 4 / -'
# 5 + ( 2 - 1 )
#p=posfix.split()
cadena='5 + ( 2 - 1 )'
# 5 2 1 - +
p=cadena.split()
infix1=[]
print(p)

def buscar():
    i=0
    while i < len(p):
        orden=prioridad(p[i])
        if orden in [1,2,3]:
            infix1.append(p[i+1])
            infix1.append(p[i-1])
            infix1.append(p[i])
        i+=1

for i in range (len(p)):
    orden=prioridad(p[i])
    print("La posición", p[i], " es prioridad: ", orden)
buscar()
print(infix1)
