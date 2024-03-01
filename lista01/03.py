# solicitar um número ao usuário e exibir todos os números pares de 0 até o número inserido

number = int(input('Insira um número inteiro: '))

for i in range(number + 1):
    if i % 2 == 0:
        print(i)