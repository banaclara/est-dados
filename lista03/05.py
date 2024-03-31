# criar uma lista de palavras e exibir a quantidade de palavras que começam com a letra 'A'

lista_palavras = ['laranja', 'limão', 'amora', 'morango', 'mirtilo', 'abacaxi', 'acerola', 'melão', 'pêra']

inicial_a = [palavra for palavra in lista_palavras if palavra[0].lower() == 'a']

print(f'A lista possui {len(inicial_a)} palavras com a inicial "a".')
print(inicial_a)