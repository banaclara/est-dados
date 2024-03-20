# criar lista de números inteiros e exibir a soma de todos

lista_inteiros = list(range(5, 30, 5))

def somar_numeros(lista):
    soma = 0
    for n in range(len(lista)):
        soma += lista[n]
    return soma

print(f'A soma dos números é {somar_numeros(lista_inteiros)}') # sum(lista_inteiros)
print(lista_inteiros)