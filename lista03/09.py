# criar duas listas de n inteiros e exibir os n que estão em ambas

lista1 = list(range(5, 100, 5))
lista2 = list(range(3, 100, 3))

lista_n = [n for n in lista1 if n in lista2 and n in lista1]

print(lista_n)