# criar a classe Círculo com o atributo Raio e implementar o método Calcular Área

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        return area

circ = Circulo(float(input('Qual o raio do círculo em cm? ')))

print(f'A área do círculo é: {circ.calcular_area():.2f}cm²')