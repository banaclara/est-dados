# função que aceita um vetor de números int e remove todos os elementos duplicados
# retornar vetor sem duplicatas

vetor_int = [5, 5, 5, 10, 5, 10, 5, 76, 90, 10, 15, 5, 25, 37, 8, 82, 54, 8, 48]

def sem_duplicatas(vetor):
    novo = []
    for n in vetor:
        if n not in novo:
            novo.append(n)
    return novo

print(sem_duplicatas(vetor_int))