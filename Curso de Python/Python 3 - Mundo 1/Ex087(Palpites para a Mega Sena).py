from random import randint
from time import sleep
lista = []
jogo = []
print('-'*30)
print(f'{'JOGO DA MEGA SENA':^30}')
print('-'*30)
qnt = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qnt:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 4,f' SOTEANDO {qnt} JOGOS ','-=' * 4)
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}:{l}')
    sleep(1)
print('-=' * 4,' =>BOA SORTE<= ','-=' * 4)