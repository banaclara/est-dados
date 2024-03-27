# encontrar elemento máximo e elemento mínimo em um vetor de int não ordenado (sem max() e min())

vetor_int = [76, 90, 10, 15, 25, 37, 82, 54, 48]

def maximo_minimo(vetor, key=''):
    if not key:
        return 'A chave é obrigatória.'
    if key == 'max':
        maior = vetor[0]
        for i in range(len(vetor)):
            if vetor[i] > maior:
                maior = vetor[i]
        return maior
    elif key == 'min':
        menor = vetor[0]
        for i in range(len(vetor)):
            if vetor[i] < menor:
                menor = vetor[i]
        return menor
    else:
        return 'Chave inválida.'
    

print(maximo_minimo(vetor_int, 'max'))