# ler uma lista de números e retornar a média dos números pares

numlist = []
pareslist = []
mediapares = 0

continuar = True

while continuar == True:
    number = int(input('Insira um número na lista: '))
    numlist.append(number)
    add_mais = input('Deseja adicionar mais números? [S/N] ').upper()
    if add_mais == 'N':
        continuar = False
    else:
        continuar = True

for i in numlist:
    if i % 2 == 0:
        mediapares += i
        pareslist.append(i)

mediapares = mediapares / len(pareslist)

print(f'A média dos números pares da lista é {mediapares:.2f}.')