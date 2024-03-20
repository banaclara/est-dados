# criar lista de strings e exibir a palavra mais longa

lista_str = ['desenhar', 'programar', 'escrever', 'projetar', 'pintar', 'fotografar']

def maior_palavra(lista):
    maior = ''
    for p in lista:
        if len(p) > len(maior):
            maior = p
    return maior

print(f'A maior palavra da lista é: {maior_palavra(lista_str)}')