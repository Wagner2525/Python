p = float(input('Digite o preço do produto:'))

d = p - (p * 0.05) 

print('O valor do produto era R${} e está por R${} com 5% de desconto'.format(p, d))