# pedir um número inteiro positivo e calcular seu fatorial

number = int(input('Insira um número inteiro positivo: '))

if number < 0:
    print('O número inserido não é positivo.')
else:
    fatorial = 1
    for i in range(fatorial, number + 1):
        fatorial *= i
    print(f'{number}! = {fatorial}')