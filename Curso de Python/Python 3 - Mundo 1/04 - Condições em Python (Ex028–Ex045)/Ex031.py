v = float(input('Digite a distância em km da sua viagem: '))

if v <= 200:
    p1 = v * 0.5
    print('O preço da sua viagem foi R${:.2f}'.format(p1))
else:
    p2 = v * 0.45
    print('O preço da sua viagem foi R${:.2f}'.format(p2)) 