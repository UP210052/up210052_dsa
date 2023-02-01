cuartos= [[[False for r in range(20)] for f in range(15)] for b in range(3)]
# cuantos cuartos estan disponibles en el 15 piso y 3 edificio
disponible=0
for i in range(20):
    if cuartos[2][14][i] == False:
        disponible+=1
print(disponible)