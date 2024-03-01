# criar a classe Funcionário com atributos Nome, Salário e Cargo e implementar o método Aumentar Salário que recebe um valor % do aumento e atualiza o Salário

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumento(self):
        valor_percentual = int(input('Qual o aumento percentual que o salário receberá? '))
        self.salario = self.salario + (self.salario * (valor_percentual / 100))
        return self.salario

func = Funcionario(input('Nome do funcionário: '), float(input('Salário: ')), input('Cargo: '))

func.aumento()

print(f'O salário atualizado do funcionário {func.nome} é R${func.salario}.')