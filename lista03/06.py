# criar lista de strings e exibir a palavra mais longa

lista1 = ['desenhar', 'escrever', 'projetar', 'pintar', 'programar', 'fotografar']

lista2 = ['desenhar', 'escrever', 'projetar', 'pintar', 'estudar']

def maior_palavra(lista):
    maior = ''
    maisdeuma = []
    for p in lista:
        if len(p) > len(maior):
            maior = p
            maisdeuma = []
        elif len(p) == len(maior):
            if maior not in maisdeuma:
                maisdeuma = [maior]
            maisdeuma.append(p)
    if maisdeuma != []:
        return maisdeuma
    else:
        return maior


print(f'Palavra(s) mais longa(s): {maior_palavra(lista1)}')
print(f'Palavra(s) mais longa(s): {maior_palavra(lista2)}')