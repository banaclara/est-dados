# criar lista de n inteiros e remover os repetidos

lista_inteiros = [1, 2, 3, 4, 5, 2, 3, 4, 7, 8, 9]
sem_repeticao = []

for n in lista_inteiros:
    if n not in sem_repeticao:
        sem_repeticao.append(n)

print(sem_repeticao)