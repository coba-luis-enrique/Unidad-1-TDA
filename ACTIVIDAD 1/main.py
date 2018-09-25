#Actividad 3
#Operacion entre conjuntos
#Coba Kaul Luis Enrique

from operacion import *

archivo = open('numero1.txt', 'r')
r = archivo.readlines()
archivo.close()

archivo2 = open('numero2.txt', 'r')
r2 = archivo2.readlines()
archivo2.close()

for lista in r:
    # revisamos si tiene un salto de linea al final para quitarlselo.
    if lista[-1] == "\n":
        dato = lista[:-1].split(",")
    else:
        dato = lista.split(", ")
    numero=int(lista)


for lista2 in r2:
    if lista2[-1] == "\n":
        dato = lista2[:-1].split(",")
    else:
        dato = lista2.split(", ")
        numero2=int(lista2)

    prototipo = operaciones(numero,numero2)

    print("ACTIVIDAD NUMEROS POSITIVOS CON CERO: ")
    print("Selecciona una opción: ")
    print("\t1 - Inicio")
    print("\t2 - Salida")
        # solicituamos una opción al usuario
    opcionMenu = input("\ninserte de una opcion>> ")

    if opcionMenu=="1":
        print("mis dos valores")
        print("valor 1: ",numero)
        print("valor 2:",numero2)
        print("1.- Cero")
        print("2.- Es cero (0==0?)")
        print("3.- El sucesor del numero es: ")
        print("4.- es igual a cero (n==0?) ")
        print("5.- Es igual Numero 1 a Numero 2: ")
        print("6.- Suma entre dos Numeros: ")
        print("7.- Antecesor de un numero: ")
        print("8.- La diferencia entre dos numeros es: ")
        print("9 .- El numero menor entre dos numeros es: ")

        opcionsubMenu = input("Digite una opcion: ")
        if opcionsubMenu=="1":
            prototipo.cero()
        elif opcionsubMenu=="2":
            prototipo.escero()
        elif opcionsubMenu=="3":
            prototipo.sucesor()
        elif opcionsubMenu=="4":
            prototipo.verificar_cero()
        elif opcionsubMenu=="5":
            prototipo.igual()
        elif opcionsubMenu=="6":
            prototipo.suma()
        elif opcionsubMenu=="7":
            prototipo.antecesor()
        elif opcionsubMenu=="8":
            prototipo.diferencia()
        elif opcionsubMenu=="9":
            prototipo.menor()
        else:
            print("Opcion incorrecta...")

    elif opcionMenu=="2":
        break
    else:
        input("Opcion incorrecta")