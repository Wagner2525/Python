from random import randint
pc = randint(0, 10)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

certo = False
cont = 0

while not certo:
    jogador = int(input('Qual é seu palpite? '))
    cont += 1
    if jogador == pc:
        certo = True
    else:
        if pc > jogador:
            print('Mais... Tente mais uma vez')
        elif jogador > pc:
            print('Menos.. Tente mais uma vez.')

print('O pc pensou {}. Você acertou com {} tentativas'.format(pc, cont))
