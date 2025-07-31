import moeda

p = float(input('Digite o preço: R$'))

while True:
    print('\n' + '-' * 30)
    print('MENU DE OPÇÕES'.center(30))
    print('-' * 30)
    print('[1] Aumentar')
    print('[2] Diminuir')
    print('[3] Dobro')
    print('[4] Metade')
    print('[0] Sair')

    r = input('Escolha o que deseja fazer: ')
    
    if r == '1':
        a = float(input('De quantos % é o aumento? '))
        resultado = moeda.aumentar(p, a)
        print(f'Aumentando {a}%, temos R${resultado:.2f}')
    elif r == '2':
        d = float(input('De quantos % é o desconto? '))
        resultado = moeda.diminuir(p, d)
        print(f'Com o desconto de {d}%, temos R${resultado:.2f}')
    elif r == '3':
        resultado = moeda.dobro(p)
        print(f'O dobro de R${p:.2f} é R${resultado:.2f}')
    elif r == '4':
        resultado = moeda.metade(p)
        print(f'A metade de R${p:.2f} é R${resultado:.2f}')
    elif r == '0':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.')

    resp = input('\nQuer fazer outra operação? [S/N] ').strip().upper()
    if resp != 'S':
        print('Encerrando...')
        break
