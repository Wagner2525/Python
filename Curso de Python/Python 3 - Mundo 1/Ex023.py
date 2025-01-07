num = int(input('Informe um número: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Número: {} \nUnidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(num, unidade, dezena, centena, milhar))