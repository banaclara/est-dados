# criar classe Pessoa com atributos Nome e Idade e implementar o método Falar imprimindo uma mensagem com o nome da pessoa

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'Olá, {self.nome}!')


pessoa = Pessoa(input('Nome: '), int(input('Idade: ')))

pessoa.falar()