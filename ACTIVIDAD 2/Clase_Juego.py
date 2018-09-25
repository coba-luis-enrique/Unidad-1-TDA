#clase de la actividad 2

class juego:
    def __init__(self, palabras):
        self.palabras = palabras

    def ObtenerPalabra(self):
        palabra_escogida=(random.choice(self.palabras))
        return palabra_escogida

    def validar_respuesta(self):
      # self.palabra=palabra
       tupalabra = " "
       intentos = 6
       print("La palabra es: ")
       while intentos > 0:
           fallas = 0
           for letra in self.palabras:
              if letra in tupalabra:
                   print(letra, end="")
              else:
                   print("x", end="")
                   fallas += 1
           if fallas == 0:
              print("\nEN HORABUENA ADIVINASTE LA PALABRA!!!")
              break

           tuletra = input("\nIngrese una letra: ")
           tupalabra += tuletra

           if tuletra not in self.palabras:
             intentos -= 1
             print("intente de nuevo")
             print("tienes", +intentos, "vidas")
           if intentos == 0:
              print("\nNO HAS ADIVINADO LA PALABRA!!!")
              print("la palabra es: ",palabras)
       else:
               print("Gracias por jugar ")
