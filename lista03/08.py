# criar lista de n inteiros e exibir os n ímpares

lista_numeros = list(range(5, 55, 5))

def impares(lista):
    impares = [n for n in lista if n % 2 != 0]
    print(impares)

impares(lista_numeros)