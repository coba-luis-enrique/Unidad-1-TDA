"""se define la clase"""

class Conjuntos:  #operaciones (identacion)

    def __init__(self,conjunto_A,conjunto_B):
        self.conjunto_A=conjunto_A
        self.conjunto_B=conjunto_B

    def eliminar_1(self):
        print("has seleccionado eliminar un elemento")
        print("conjunto A= ",self.conjunto_A)
        numero = int(input("introduzca el elemento")) #Espeficamos enteros
        self.conjunto_A.discard(numero)  # Metodo que elimina un numero a un set
        print("conjunto A= ",self.conjunto_A)

    def eliminar_2(self):
        print("has seleccionado eliminar un elemento")
        print("conjunto B=",self.conjunto_B)
        numero = int(input("introduzca el elemento: "))
        self.conjunto_B.discard(numero)  # Metodo que elimina un elemento a un set
        print("conjunto B=",self.conjunto_B)

    def agregar_1(self):
        print("has seleccionado agregar  elemento")
        print("conjunto A=",self.conjunto_A)
        numero = int(input("introduzca el elemento: "))
        self.conjunto_A.add(numero)  # Metodo que agrega un elemento a un set
        print("conjunto A=",self.conjunto_A)
    def agregar_2(self):
        print("has seleccionado agregar un elemento")
        print("conjunto B=",self.conjunto_B)
        numero = int(input("introduzca el elemento "))
        self.conjunto_B.add(numero)  # Metodo que agrega un elemento a un set
        print("conjunto B=",self.conjunto_B)
    def union(self):
        print("has seleccionado la union entre dos conjuntos")
        print("conjunto A=",self.conjunto_A)
        print("conjunto B=",self.conjunto_B)
        print("union=",self.conjunto_A.union(self.conjunto_B)) #metodo que une dos sets(conjuntos
    def interseccion(self):
        print("has seleccionado la interseccion entre dos conjuntos")
        print("conjunto A=",self.conjunto_A)
        print("conjunto B=",self.conjunto_B)
        print("diferencia=",self.conjunto_A & self.conjunto_B) #metodo que busca elementos iguales en dos conjuntos
    def diferencia_A(self):
        print("has seleccionado buscar la diferencia del conjunto")
        print("conjunto A=",self.conjunto_A)
        print("conjunto B=",self.conjunto_B)
        print("diferencia=",self.conjunto_A - self.conjunto_B) #metodo que busca la diferencia en dos conjuntos
    def diferencia_B(self):
        print("has seleccionado buscar la diferencia del conjunto")
        print("conjunto A=",self.conjunto_A)
        print("conjunto B=",self.conjunto_B)
        print("diferencia=",self.conjunto_B - self.conjunto_A)
    def verificar_A(self):
        print("has seleccionado verificar si un elemento pertenece al conjunto A")
        print("conjunto A=",self.conjunto_A)
        numero = int(input("introduzca un elemento: ")) #Metodo que si un elemento pertenece a cierto conjunto
        print(numero in self.conjunto_A)
    def verificar_B(self):
        print("has seleccionado verificar si un elemento pertenece al conjunto B")
        print("conjunto B=",self.conjunto_B)
        numero = int(input("introduzca un elemento: "))
        print(numero in self.conjunto_B)
    def conjunto_vacio(self):
        print("has seleccionado el conjunto vacio")
        set_empty = set() # conjunto vacio #define conjunto vacio
    def esvacio(self):

        if self.conjunto_A==set():
            print("correcto")
        else:
            print("el conjunto no esta vacio")
