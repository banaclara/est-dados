# criar a classe Triângulo com atributos Lado1, Lado2, Lado3 e implementar o método Calcular Perímetro

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_perimetro(self):
        p = self.a + self.b + self.c
        return p
    

tri = Triangulo(int(input('Lado 1: ')), int(input('Lado 2: ')), int(input('Lado 3: ')))

print(f'O perímetro do triângulo é {tri.calcular_perimetro()}cm²')