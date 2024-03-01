# criar a classe Livro com os atributos Título e Autor e implementar o método Detalhes com as informações do Livro

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_detalhes(self):
        print(f'Livro: {self.titulo} \nAutor: {self.autor}')

livro = Livro(input('Digite o título do livro: '), input('Digite o nome do autor do livro: '))

livro.mostrar_detalhes()