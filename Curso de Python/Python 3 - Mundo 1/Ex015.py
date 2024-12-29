km = float(input('Qual foi a quantidade de km percorrida? '))
dias = int(input('Digite a quantidade de dias locados:'))

k = km * 0.15
d = dias * 60
p = k + d

print('O preço a pagar é {}'.format(p))