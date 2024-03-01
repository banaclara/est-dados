# calcular média de 3 números inseridos pelo usuário
def media(first, second, third):
    media = (first + second + third) / 3
    return media

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

resultado = media(num1, num2, num3)
print(f'A média dos três números é {resultado:.2f}')