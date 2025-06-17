print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Valor que deseja sacar: R$'))
total = valor
dinheiro_do_caixa = 50
totaldin = 0

while True:
    if total >= dinheiro_do_caixa:
        total -= dinheiro_do_caixa
        totaldin += 1
    else:
        if totaldin > 0:
            print(f'Total de {totaldin} cédulas de R${dinheiro_do_caixa}')
        if dinheiro_do_caixa == 50:
            dinheiro_do_caixa = 20
        elif dinheiro_do_caixa == 20:
            dinheiro_do_caixa = 10
        elif dinheiro_do_caixa == 10:
            dinheiro_do_caixa = 1
        totaldin = 0
        if total == 0:
            break
