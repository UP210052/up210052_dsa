# son cuatro tipos de funciones 
# pip install numpy
# map mapealo estructuralo
# filter filtro
y=(lambda x:x+3)(4)
print(y)

def potencia(base, exponenete=2): # solo toma el 2 cuando no le mandas un valor
    return base * exponenete

def cuadratica(a,b=-8,c=15):
    return (-b + (b**2 - 4*a*c) **.5 )/ (2*a)
y=cuadratica(1)
print(y)

# None no tiene valor.
a= None
b= True if a==None else False

#guarda la direcciones cuando lo manadas a funcion un vector.
#  \ toma lo siguente pero sin espacio
# tuplas y diccionarios ()
# tupla no se puede modificar, nada mas leibles 
t1 = (1,0)
t2 = (5,6)
t1, t2 = t2,t1
print(t1)
print(t2)
# vectores []
#Diccionarios = { clave : valor } , se busca con base a la clave.

assert y==1
# aseguar si y==1 sigue con el programa
try:
    y=5/0
    print("Hola")
except:
    print("error")
finally:
    print("Cool")