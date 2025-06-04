v = float(input('Digite o valor do protudo: R$'))
print('''Digite a forma de pagamento!
          [1] À vista dinheiro/cheque (10% de desconto)
          [2] À vista no cartão       (5% de desconto)
          [3] Em até 2x no cartão     (preço formal)
          [4] 3x ou mais no cartão    (20% de juros)''')
op = int(input('Sua opção: '))

if op == 1:
    f = v * 0.9
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(v,f))
elif op == 2:
    f = v * 0.95
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(v,f))
elif op == 3:
    print('Sua compra será parcelada em 2x!'.format(p))
    print('Sua compra vai custar o valor real!'.format(v,f))
elif op == 4:
    f = v * 1.2
    p = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS!'.format(p, (f/p)))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(v,f))
else:
     print('Essa opção não existe!')