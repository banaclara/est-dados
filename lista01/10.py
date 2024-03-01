# pedra, papel, tesoura entre usuário x computador

import random

ppt = ['pedra', 'papel', 'tesoura']

user = input('Pedra, Papel ou Tesoura? ').lower()
computador = random.choice(ppt)

if user == 'pedra' and computador == 'papel' or user == 'tesoura' and computador == 'pedra' or user == 'papel' and computador == 'tesoura':
    print(f'O computador escolheu {computador}. Você perdeu!')
elif user == computador:
    print(f'Empate. Ambos escolheram {user}.')
else:
    print(f'O computador escolheu {computador}. Você ganhou!')