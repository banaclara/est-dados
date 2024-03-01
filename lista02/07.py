# criar a classe Carro com os atributos Marca, Modelo e Ano e implementar um método Detalhes que mostra as informações do carro

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_detalhes(self):
        print(f'{self.marca} \n{self.modelo} \n{self.ano}')

carro = Carro(input('Marca: '), input('Modelo: '), int(input('Ano: ')))

carro.mostrar_detalhes()