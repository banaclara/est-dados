# imprimir a sequência de Fibonacci até o valor inserido pelo usuário

number = int(input('Insira um número inteiro positivo: '))

fiblist = [0, 1]

while fiblist[-1] <= number:
    fiblist.append(fiblist[-1] + fiblist[-2])

if fiblist[-1] > number:
    fiblist.remove(fiblist[-1])

print(fiblist)