# função para ordenar um vetor de int que recebe um parâmetro como chave para ordenação crescente ou decrescente

vetor_int = [90, 10, 15, 25, 37, 82, 54, 48]

def ordenar_vetor(vetor, key=''):
    if not key:
        return 'A chave é obrigatória.'
    for i in range(len(vetor) - 1):
        n = i
        if key == 'crescente':
            for j in range(i+1, len(vetor)):
                if vetor[n] > vetor[j]:
                    n = j
        elif key == 'decrescente':
            for j in range(i+1, len(vetor)):
                if vetor[n] < vetor[j]:
                    n = j
        else:
            return 'Chave inválida'
        auxiliar = vetor[i]
        vetor[i] = vetor[n]
        vetor[n] = auxiliar
    return vetor


print(ordenar_vetor(vetor_int))
print(ordenar_vetor(vetor_int, 'decrescente'))
print(ordenar_vetor(vetor_int, 'crescente'))