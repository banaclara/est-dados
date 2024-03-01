# verificar se um número é primo

number = int(input('Insira um número inteiro positivo: '))

naoprimo = 0

for i in range(2, number):
    if number % i == 0:
        naoprimo += 1

if naoprimo == 0:
    print(f'{number} é um número primo.')
else:
    print(f'{number} NÃO é um número primo.')