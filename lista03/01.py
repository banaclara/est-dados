# criar uma lista de números inteiros e exibir o maior número

lista1 = list(range(5, 90, 5))
lista2 = [10, 20, 80, 15, 90, 25]

def maior_numero(lista_inteiros):
    maior = 0
    for i in lista_inteiros:
        if i > maior:
            maior = i
    return maior

print(f'O maior número em {lista1} é {maior_numero(lista1)}') # max(lista1)
print(f'O maior número em {lista2} é {maior_numero(lista2)}') # max(lista2)