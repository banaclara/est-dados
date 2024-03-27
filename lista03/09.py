# criar duas listas de n inteiros e exibir os n que estão em ambas

lista1 = list(range(5, 100, 5))
lista2 = list(range(3, 100, 3))

def idem(umalista, outralista):
    idem = [n for n in umalista if n in outralista]
    return idem

print(idem(lista1, lista2))