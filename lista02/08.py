# criar a classe Aluno com atributos Nome e Notas e implementar o método Calcular Média

class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        return media
    

aluno = Aluno(input('Nome do aluno: '), int(input('Primeira nota: ')), int(input('Segunda nota: ')), int(input('Terceira nota: ')))

print(f'Média de {aluno.nome}: {aluno.calcular_media()}')