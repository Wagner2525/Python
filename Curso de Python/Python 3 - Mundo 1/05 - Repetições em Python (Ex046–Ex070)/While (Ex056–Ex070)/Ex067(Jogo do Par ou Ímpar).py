from random import randint
c = 0

print('=-'*13)
print('Vamos jogar PAR or ÍMPAR')

while True:
    print('**'*13)
    n = int(input('Diga um valor: '))
    pc = randint(0, 11)
    s = n + pc
    j = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('**'*13)

    if s % 2 == 0:
        if j in 'Pp':
            c += 1
            print(f'Você jogou {n} e o pc jogou {pc}. Total deu {s} DEU PAR!!')
            print('Você ganhou! Parabéns!!!')
        if j in 'Ii':
            print(f'Você jogou {n} e o pc jogou {pc}. Total deu {s} DEU PAR!!')
            print('Você perdeu!')
            break
    if s % 3 == 0:
        if j in 'Ii':
            c += 1
            print(f'Você jogou {n} e o pc jogou {pc}. Total deu {s} DEU ÍMPAR!!')
            print('Você ganhou! Parabéns!!!')
        if j in 'Pp':
            print(f'Você jogou {n} e o pc jogou {pc}. Total deu {s} DEU ÍMPAR!!')
            print('Você perdeu!')
            break
    print('Vamos jogar de novo...')
print(f'Game Over!!! Você venceu {c} vezes')
            