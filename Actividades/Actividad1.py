conjunto1={}
conjunto2={}

def union_conjuntos(conjunto1,conjunto2):
    union1 = conjunto1.union(conjunto2)
    print(union1)

def interseccion(conjunto1,conjunto2):
    interseccion = conjunto1.intersection(conjunto2)
    print(interseccion)

conjunto1 = set(input("Ingrese los elementos del conjunto 1 separados por comas: ").split(","))
conjunto2 = set(input("Ingrese los elementos del conjunto 2 separados por comas: ").split(","))

opc=int(input('Seleccione una opcion:\n1.- Union de conjuntos\n2.- Interseccion de conjuntos\n'))
if opc==1:
    union_conjuntos(conjunto1,conjunto2)
elif opc==2:
    interseccion(conjunto1,conjunto2)
else:
    print('Opcion no valida')