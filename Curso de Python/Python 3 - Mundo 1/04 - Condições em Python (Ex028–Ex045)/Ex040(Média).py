n1 = float(input('Digite a sua 1º nota:'))
n2 = float(input('Digite a sua 2º nota:'))
m = (n1 + n2) / 2

print('Sua média foi de {:.1f} '.format(m))
if m < 5:
    print('REPROVADO!')
elif m > 5 and m <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
