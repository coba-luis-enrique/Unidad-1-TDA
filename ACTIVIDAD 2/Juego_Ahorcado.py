#Coba Kauil Luis Enrique
#actividad 2

import random #libreria para buscar palabras en aleatorio
import time
from Clase_Juego import juego  #importa los metodos de la clase

palabras=['matematica','fisica','quimica','filosofia','medicina','sociologia',
    'psicologia','estadistica','aeronautica','hidraulica','estatica','dinamica',
    'hidrologia','topografia','geografia','geodesia','construccion','estructuras',
    'instalaciones','electronica','programacion','economia','presupuestos','practica'
]
palabra_azar = random.choice(palabras)

jugar=juego(palabra_azar)#objeto

print("Juego del ahorcado: ")
print("Selecciona una opción: ")
print("\t1 - Inicio")
print("\t2 - Salida")
# solicituamos una opción al usuario
opcionMenu = input("\ninserte de una opcion>> ")

if opcionMenu == "1":
    print("debes de esperar 4 segundos para que el juego empiece :)")
    time.sleep(4)
    jugar.validar_respuesta()# jugar.adivinar(palabra) #procediemiento para adivinar la palabra

elif opcionMenu== "2":
    print("finalizado...")

else:
    input("Opcion incorrecta")

