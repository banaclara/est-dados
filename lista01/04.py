# ler uma lista de números e exibir o maior e o menor

numlist = []

continuar = True

while continuar == True:
    number = int(input('Insira um número na lista: '))
    numlist.append(number)
    add_mais = input('Deseja adicionar mais números? [S/N] ').upper()
    if add_mais == 'N':
        continuar = False
    else:
        continuar = True

print(f'O maior número da lista é {max(numlist)}.')
print(f'O menor número da lista é {min(numlist)}.')