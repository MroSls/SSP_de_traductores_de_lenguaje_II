#Notaciones
notacion=['<real>:=', '<entero>', '<enteroconsigno>', '<enterosinsigno>', '<fraccion>', '<digito>', '.', '-', '']

#Entrada
entrada = input('Ingrese un numero: ')

#Funciones
def conguion(entrada, fraccion):
    print(notacion[0]+notacion[1]+fraccion+'\n'+notacion[0]+notacion[2]+fraccion+'\n'+notacion[0]+notacion[7]+notacion[3]+fraccion)
    salida=notacion[7]
    for i in entrada.split(notacion[7])[1]:
        salida=salida+notacion[5]
    return salida

def conentero(entrada,fraccion):
    salida=''
    print(notacion[0]+notacion[1]+fraccion+'\n'+notacion[0]+notacion[3]+fraccion)
    for i in entrada:
        salida=salida+notacion[5]
    return salida

def conpunto(entrada,salida):
    salida= notacion[0]+salida
    print(salida+notacion[4]+'\n'+salida+notacion[6]+notacion[3])
    salida=salida+notacion[6]
    for i in entrada:
        salida=salida+notacion[5]
    return salida

#Validaciones
if notacion[6] in entrada:#Si la entrada tiene punto
    entrada = entrada.split(notacion[6])
    if notacion[7] in entrada[0]:#Si la entrada tiene guion
        print(conpunto(entrada[1],conguion(entrada[0], notacion[4])))
    elif entrada[0].isdigit():#Si la entrada es solo numeros sin signos
        print(conpunto(entrada[1],conentero(entrada[0], notacion[4])))
    else:
        print(conpunto(entrada[1],notacion[8]))

elif notacion[7] in entrada:#Si la entrada tiene guion
    print(notacion[0]+conguion(entrada,notacion[8]))

elif entrada.isdigit():#Si la entrada es solo numeros sin signos
    print(notacion[0]+conentero(entrada,notacion[8]))

else:#Si la entrada no es un numero
    print('No se puede procesar la entrada')