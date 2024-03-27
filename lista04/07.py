# criar função que aceite um vetor de int e retorne o terceiro maior número ainda que existam n duplicados

vetor_int = [5, 5, 5, 10, 5, 10, 5, 76, 90, 90, 90, 10, 15, 5, 25, 37, 8, 82, 82, 54, 8, 48]

def terceiro_maior(vetor):
    maior = vetor[0]
    for n in vetor:
        if n > maior:
            maior = n
    while maior in vetor:
        vetor.remove(maior)

    maior2 = vetor[0]
    for n in vetor:
        if n > maior2:
            maior2 = n
    while maior2 in vetor:
        vetor.remove(maior2)

    maior3 = vetor[0]
    for n in vetor:
        if n > maior3:
            maior3 = n
    return maior

print(terceiro_maior(vetor_int))