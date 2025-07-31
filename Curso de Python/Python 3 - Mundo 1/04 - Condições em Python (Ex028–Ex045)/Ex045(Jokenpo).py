from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
      [0] Pedra
      [1] PAPEL
      [2] TESOURA''')

op = int(input('Qual vai ser a sua jogada? '))
pc = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)

print('-=-' * 8)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[op]))
print('-=-' * 8)

if pc == 0: #PEDRA
    if op == 1:
        print('O jogador ganhou!')
    elif op == 2:
        print('O computador ganhou!')
    elif op == pc:
        print('Empate!!')
elif pc == 1: #PAPEL
    if op == 2:
        print('O jogador ganhou!')
    elif op == 0:
        print('O computador ganhou!')
    elif op == pc:
        print('Empate!!')
elif pc == 2: #TESOURA
    if op == 1:
        print('O computador ganhou!')
    elif op == 0:
        print('O jogador ganhou!')
    elif op == pc:
        print('Empate!!')
