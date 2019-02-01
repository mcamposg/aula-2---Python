import math

class Retangulo:
    contador = 0

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        Retangulo.contador += 1

    def area(self):  # Método da classe
        return self.largura * self.altura

    def diagonal(self):
        return math.sqrt(self.largura ** 2 + self.altura ** 2)

class Quadrado(Retangulo):  # Quadrado é um subtipo de Retangulo
    #contador = 0
    def __init__(self, lado):
        self.largura = lado
        self.altura = lado
        Quadrado.contador += 1

quad = Quadrado(1)
#print(quad.area())
#print(quad.diagonal())

ret = Retangulo(3, 4)
#print(ret.area())
#print(ret.diagonal())

ret2 = Retangulo(4, 5)
print(ret2.diagonal())
ret2.altura = 8
print(ret2.diagonal())

quad2 = Quadrado(2)
quad3 = Quadrado(3)

print("Retangulos:", Retangulo.contador)
print("Quadrados:", Quadrado.contador)

print("Retangulos:", Retangulo.contador)
print("Quadrados:", Quadrado.contador)
