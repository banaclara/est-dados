# ler uma lista de nomes e retornar uma nova lista apenas com os nomes que comecem com a letra 'A'

namelist = []

continuar = True

while continuar == True:
    number = input('Insira um nome na lista: ')
    namelist.append(number)
    add_mais = input('Deseja adicionar mais números? [S/N] ').upper()
    if add_mais == 'N':
        continuar = False
    else:
        continuar = True

nomescomA = []

for nome in namelist:
    if nome[0] == 'a' or nome[0] == 'A':
        nomescomA.append(nome)

print(f'Nomes da lista que começam com a letra "A": {nomescomA}')