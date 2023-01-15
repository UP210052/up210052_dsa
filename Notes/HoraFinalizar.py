horas = int(input("Dame las horas: "))
minutos = int(input("Dame los minutos: "))
duracion = int(input("Dame la duracion: "))
horasFinal= (horas + ((minutos+duracion) // 60)) % 24
minutosFinal= (minutos+duracion) % 60
print (horasFinal,":",minutosFinal)