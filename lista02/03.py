# criar a classe Retângulo com os atributos Base e Altura e implementar o método Calcular Área

class Retangulo:
    def __init__(self, h, b):
        self.h = h
        self.b = b

    def calcular_area(self):
        area = self.h * self.b
        return area

ret = Retangulo(float(input('Base do retângulo em cm: ')), float(input('Altura do retângulo em cm: ')))

print(f'A área do retângulo é: {ret.calcular_area():.2f}cm²')