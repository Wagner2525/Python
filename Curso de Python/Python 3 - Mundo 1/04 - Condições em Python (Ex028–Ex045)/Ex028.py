import random
from time import sleep

print('-=-' * 20)
print('Jogo da adivinhação')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

num = int(input('Digite um numero: '))
pc = random.randint(0, 5)
print('PENSANDO...')
sleep(2)

if num == pc:
    print('Você acertou. Parabéns!!!')
else:
    print('Que pena, você errou. :/ \nO número era {}'.format(pc))