print('=' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('=' * 30)

s = cont = tot1 = menor = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    p = float(input('Preço: R$'))

    cont += 1
    s += p

    if p > 1000:
        tot1 += 1

    if cont == 1 or p < menor:
        menor = p
        barato = nome

    while True:
        flag = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if flag in 'SN':
            break
    if flag == 'N':
        break
print(f'O total gasto foi de {s}')
print(f'{tot1} produtos valem mais de 1k')
print(f'O produto mais barato: {barato}')