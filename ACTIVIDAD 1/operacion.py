"""se define la clase"""

class operaciones:  #operaciones (identacion)

    def __init__(self,num, num2):
        self.num=num;
        self.num2=num2;

    def cero(self):
        print("0")

    def suma(self):
        print(self.num+self.num2)

    def diferencia(self):
        print(self.num - self.num2)

    def verificar_cero(self):
        if self.num == 0:
            print(self.num,"si es igual a cero")
        else:
            print(self.num,"no es igual a cero")

    def sucesor(self):
        print(self.num+1)

    def antecesor(self):
        print(self.num-1)

    def igual(self):
        if self.num == self.num2:
            print("si es igual")
        else:
            print("no es igual")

    def escero(self):
        print(0 * 0)

    def menor(self):
        if self.num < self.num2:
            print(self.num)
        else:
            print(self.num2)
