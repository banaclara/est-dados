# criar função que receba um vetor de int e retorne a mediana
# funcionar para len(vetor) % 2 != 0

vetor_int = [5, 5, 5, 10, 5, 10, 5, 76, 90, 90, 90, 10, 15, 5, 25, 37, 8, 82, 82, 54, 8, 48, 40]

def ordenar(vetor):
    if len(vetor) <= 1:
        return vetor
    pivot = vetor[len(vetor) // 2]
    inicio = [n for n in vetor if n < pivot]
    meio = [n for n in vetor if n == pivot]
    fim = [n for n in vetor if n > pivot]
    return ordenar(inicio) + meio + ordenar(fim)

def mediana(vetor):
    ordenado = ordenar(vetor)
    if len(ordenado) % 2 == 0:
        mediana = (ordenado[len(ordenado) // 2 - 1] + ordenado[len(ordenado) // 2]) / 2
    else:
        mediana = ordenado[len(ordenado) // 2]
    return mediana

print(mediana(vetor_int))