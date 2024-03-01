# criar a classe Conta Bancária com os atributos Saldo e Titular e implementar os métodos Depositar e Sacar

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        deposito = float(input('Valor do depósito: '))
        self.saldo += deposito
        return self.saldo
    
    def sacar(self):
        saque = float(input('Valor do saque: '))
        self.saldo -= saque
        return self.saldo
    

conta = ContaBancaria(input('Nome do titular: '), float(input('Saldo: ')))

conta.depositar()
conta.sacar()

print(f'Saldo atual: {conta.saldo}')