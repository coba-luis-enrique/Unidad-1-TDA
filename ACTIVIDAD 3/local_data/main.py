#Actividad 3
#Operacion entre conjuntos
#Coba Kaul Luis Enrique


""""En Python casi todo es un objeto, a diferencia de
otros lenguajes, un clase es un objeto también,
suena raro pero efectivamente es así:"""

import os
from Operacion import *

set_one={9,6,5,2,7,10} #Definir un conjunto, empleamos sets
set_two={12,7,4,10,11}


print("Selecciona una opción: ")
print("\t1 - Eliminar un elemento de un conjunto")
print("\t2 - Ingresar un elemento a un conjunto")
print("\t3 - Union de conjuntos")
print("\t4 - interseccion de dos conjuntos")
print("\t5 - diferencia de dos conjuntos")
print("\t6 - Pertenece un elemento a un conjunto")
print("\t7 - conjunto vacio")
print("\t8 - Esvacio")
print("\t9 - salir")

prototipo = Conjuntos(set_one,set_two)

while True:

    # solicituamos una opción al usuario

    opcionMenu = input("\ninserte de una opcion>> ")

    if opcionMenu == "1":
        print("\t1 - Eliminar un elemento del conjunto A")
        print("\t2 - Eliminar un elemento del conjunto B")
        opcionsubMenu = input("inserte una opcion>> ")
        if opcionsubMenu=="1":
            prototipo.eliminar_1()
            print("elemento eliminado...")
        elif opcionsubMenu=="2":
            prototipo.eliminar_2()
            print("elemento eliminado...")
        else:
            print("ingresa bien los valores....")
        input("Pulsa una tecla para continuar")

    elif opcionMenu == "2":
        print("\t1 - Ingresar un elemento del conjunto A")
        print("\t2 - Ingresar un elemento del conjunto B")
        opcionsubMenu2 = input("inserte una opcion>> ")
        if opcionsubMenu2=="1":
            prototipo.agregar_1()
            print("elemento Agregado...")
        elif opcionMenu2=="2":
            prototipo.agregar_2()
            print("elemento Agregado...")
        else:
            print("ingresa bien los valores....")
        input("Pulsa una tecla para continuar")

    elif opcionMenu == "3":
        prototipo.union()
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")

    elif opcionMenu == "4":
        prototipo.interseccion()
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")

    elif opcionMenu == "5":
        print("\t1 - Diferencia del conjunto A con respecto al conjunto B")
        print("\t2 - Diferencia del conjunto B con respecto al conjunto A")
        opcionsubMenu3 = input("inserte una opcion>> ")
        if opcionsubMenu3 == "1":
            prototipo.diferencia_A()
            print("Proceso Terminado...")
        elif opcionsubMenu3 == "2":
            prototipo.diferencia_B()
            print("Proceso terminado...")
        else:
            print("ingresa bien los valores...")
        input("Pulsa una tecla para continuar")

    elif opcionMenu == "6":
        print("\t1 - Elemento que pertenece conjunto A")
        print("\t2 - Elemento pertenece al conjunto B")
        opcionsubMenu4 = input("inserte una opcion>> ")
        if opcionsubMenu4 == "1":
            prototipo.verificar_A()
            print("Proceso Terminado...")
        elif opcionMenu4 == "2":
            prototipo.vericar_B()
            print("Proceso terminado...")
        else:
            print("ingresa bien los valores...")
        input("Pulsa una tecla para continuar")

    elif opcionMenu == "7":
        prototipo.conjunto_vacio()
        input("Pulsa una tecla para continuar")

    elif opcionMenu == "8":
        prototipo.esvacio()
        input("Ppulsa una tecla para continuar")

    elif opcionMenu == "9":
        break

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")