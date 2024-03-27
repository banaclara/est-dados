# função para ordenar um vetor de int em ordem crescente
# usar algoritmo de seleção

vetor_int = [90, 10, 15, 25, 37, 82, 54, 48]

def selecao_crescente(vetor):
    for i in range(len(vetor) - 1):
        menor = i
        for j in range(i+1, len(vetor)):
            if vetor[menor] > vetor[j]:
                menor = j
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
    print(vetor)


selecao_crescente(vetor_int)