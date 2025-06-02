valor_da_casa = float(input('Digite o valor da casa:'))
salario =  float(input('Digite o seu salário:'))
anos = int(input('Digite o tempo (anos) que deseja pagar:'))
p = valor_da_casa/(anos*12)

if anos >= 50:
    print('\nAnálise do financiamento...')
    print('✅ Empréstimo APROVADO!')
    print('Sua prestação foi de R${:.2f} por mês'.format(prestacao))
elif anos < 50 and p >= (salario*0.3):
    print('\nAnálise do financiamento...')
    print('❌ Empréstimo NEGADO. A prestação excede 30% do salário.')
