from random import randint
from time import sleep
def sorteia(num, lista):
    print(f'Sorteando {num} valores da lista: ', end='')
    for i in range(num):
        sorteio = randint(0, 15)
        lista.append(sorteio)
        print(f'{sorteio} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 ==0:
            soma += valor
    print(f'Somando os valores pares da {lista}, temos {soma}')

#MAIN
n_sorteio = int(input('Quantos números quer sortear? '))
números = []
sorteia(n_sorteio, números)
somaPar(números)