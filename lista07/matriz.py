sono_mes = [[8, 6, 7, 8, 6], [5, 5, 6, 7, 8], [6, 7, 8, 6, 5], [7, 5, 9, 7, 4]]

print('--- análise mensal de sono ---')

print('1 - dia da semana com maior horário de descanso:')

h_por_dia = [sum(sono_mes[y][x] for y in range(len(sono_mes))) for x in range(len(sono_mes[0]))]

def encontrar_dia(lista, func):
    if lista.index(func(lista)) == 0:
        print('Segunda-feira')
    elif lista.index(func(lista)) == 1:
        print('Terça-feira')
    elif lista.index(func(lista)) == 2:
        print('Quarta-feira')
    elif lista.index(func(lista)) == 3:
        print('Quinta-feira')
    else:
        print('Sexta-feira')

encontrar_dia(h_por_dia, max)

print('---')
print('2 - dia da semana com menor horário de descanso:')

encontrar_dia(h_por_dia, min)

print('---')
print('3 - semana com maior horário de descanso:')

h_por_semana = [sum(sono_mes[x][y] for y in range(len(sono_mes[x]))) for x in range(len(sono_mes))]

def encontrar_semana(lista, func):
    if lista.index(func(lista)) == 0:
        print('Primeira semana')
    elif lista.index(func(lista)) == 1:
        print('Segunda semana')
    elif lista.index(func(lista)) == 2:
        print('Terceira semana')
    else:
        print('Quarta semana')

encontrar_semana(h_por_semana, max)

print('---')
print('4 - semana com menor horário de descanso:')

encontrar_semana(h_por_semana, min)

print('---')
print('5 - menor tempo de descanso:')

def encontrar_valor(lista, key=''):
    valor = lista[0][0]
    for l in lista:
        if key == "menor":
            if min(l) < valor:
                valor = min(l)
        elif key == "maior":
            if max(l) > valor:
                valor = max(l)
    return valor

menor_tempo = encontrar_valor(sono_mes, 'menor')

print(f'{menor_tempo}h')

print('---')
print('6 - maior tempo de descanso:')

maior_tempo = encontrar_valor(sono_mes, 'maior')
print(f'{maior_tempo}h')

print('---')
print('7 - quantos dias da semana com o menor tempo de descanso:')

dias_menor_t = 0
for l in sono_mes:
    dias_menor_t += l.count(menor_tempo)
print(f'{dias_menor_t} dia(s) com {menor_tempo}h de descanso')

print('---')
print('8 - quantos dias da semana com o maior tempo de descanso:')

dias_maior_t = 0
for l in sono_mes:
    dias_maior_t += l.count(maior_tempo)
print(f'{dias_maior_t} dia(s) com {maior_tempo}h de descanso')

print('---')
print('9 - % por semana em relação ao total por mês')

total_mes = sum(h_por_semana)
pc_s1 = (h_por_semana[0] / total_mes) * 100
pc_s2 = (h_por_semana[1] / total_mes) * 100
pc_s3 = (h_por_semana[2] / total_mes) * 100
pc_s4 = (h_por_semana[3] / total_mes) * 100

print(f'semana 1 -> {pc_s1:.2f}%')
print(f'semana 2 -> {pc_s2:.2f}%')
print(f'semana 3 -> {pc_s3:.2f}%')
print(f'semana 4 -> {pc_s4:.2f}%')