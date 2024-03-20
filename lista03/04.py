# criar lista de números inteiros e exibir a média dos números

lista_inteiros = list(range(10, 50, 10))

def media(lista):
    media = sum(lista) / len(lista)
    return media

print(f'A média é {media(lista_inteiros)}')
print(lista_inteiros)