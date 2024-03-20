# criar lista de n inteiros e exibir os n pares

lista_numeros = list(range(5, 55, 5))

def pares(lista):
    pares = [n for n in lista if n % 2 == 0]
    print(pares)

pares(lista_numeros)