# função que retorna o segundo menor número de um vetor de int ainda que existam números duplicados

vetor_int = [5, 5, 5, 10, 5, 10, 5, 76, 90, 10, 15, 5, 25, 37, 8, 82, 54, 8, 48]

def segundo_menor(vetor):
    menor = vetor[0]
    for n in vetor:
        if n < menor:
            menor = n
    
    if menor == vetor[0]:
        for n in vetor:
            if n > menor:
                segundomenor = n
                break
    else:
        segundomenor = vetor[0]

    for n in vetor:
        if n != menor and n < segundomenor:
            segundomenor = n
    return segundomenor


print(segundo_menor(vetor_int))