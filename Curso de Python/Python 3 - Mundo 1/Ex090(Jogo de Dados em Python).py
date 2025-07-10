from random import randint
from time import sleep
from operator import itemgetter
jogador = {'Jogador_1': randint(1,6),
           'Jogador_2': randint(1,6),
           'Jogador_3': randint(1,6),
           'Jogador_4': randint(1,6)}
rank = {}
print('VALORES SORTEADOS:')
for chave, valor in jogador.items():
    print(f'{chave} tirou {valor} no dado')
    sleep(1)
rank = sorted(jogador.items(), key= itemgetter(1), reverse= True)
print('=' * 5, ' RANKING ', '=' * 5)
for indice, valor in enumerate(rank):
    print(f'{indice + 1}º lugar: {valor[0]} com {valor[1]}')
    sleep(1)