# função para ordenar vetor de inteiros em ordem decrescente
# contar quantos n pares e quantos ímpares existem no vetor ordenado

vetor_int = [5, 5, 5, 10, 5, 10, 5, 76, 90, 10, 15, 5, 25, 37, 8, 82, 54, 8, 48]

def decrescente(vetor):
    if len(vetor) <= 1:
        return vetor
    pivot = vetor[len(vetor) // 2]
    inicio = [n for n in vetor if n > pivot]
    meio = [n for n in vetor if n == pivot]
    fim = [n for n in vetor if n < pivot]
    return decrescente(inicio) + meio + decrescente(fim)

def qtdd_pares_impares(vetor):
    ordenado = decrescente(vetor)
    impares = [n for n in ordenado if n % 2 != 0]
    pares = [n for n in ordenado if n % 2 == 0]
    print(f'Existem {len(impares)} números ímpares e {len(pares)} números pares na lista.')

qtdd_pares_impares(vetor_int)