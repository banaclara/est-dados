# criar função que aceite um vetor de int e retorne o terceiro maior número ainda que existam n duplicados

vetor_int = [5, 5, 5, 10, 5, 10, 5, 76, 90, 90, 90, 10, 15, 5, 25, 37, 8, 82, 82, 54, 8, 48]

def terceiro_maior(vetor):
    maior = vetor[0]
    segundo_maior = vetor[0]
    terceiro_maior = vetor[0]
    for n in vetor:
        if n > maior:
            maior = n
    for n in vetor:
        if n > segundo_maior and n < maior:
            segundo_maior = n
    for n in vetor:
        if n > terceiro_maior and n < segundo_maior:
            terceiro_maior = n
    return terceiro_maior

print(terceiro_maior(vetor_int))