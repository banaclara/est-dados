# criar a classe Produto com atributos Nome, Preço e Quantidade e implementar um método Calcular Total que retorna o valor total (preço * quantidade)

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        valor_total = self.preco * self.quantidade
        return valor_total
    

prod = Produto(input('Nome do produto: '), float(input('Preço: ')), int(input('Quantidade do produto em estoque: ')))

print(f'Valor total do produto em estoque: {prod.calcular_total()}')