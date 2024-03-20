# criar lista de nomes e exibir o n total de nomes

lista_nomes = []
add_mais = 'S'

while add_mais == 'S' or add_mais == 's':
    novo_nome = input('Digite um nome para inserir na lista: ')
    lista_nomes.append(novo_nome)
    add_mais = input('Adicionar outro? [S/N] ')

def contar_nomes(lista):
    n_total = 0
    for n in lista:
        n_total += 1
    return n_total

print(f'A lista possui {contar_nomes(lista_nomes)} nomes.') # len(lista_nomes)