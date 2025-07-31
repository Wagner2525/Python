import moeda_107

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
        resultado = moeda_107.aumentar(p, a)
        print(f'Aumentando {a}%, temos {moeda_107.moeda(resultado)}')
    elif r == '2':
        d = float(input('De quantos % é o desconto? '))
        resultado = moeda_107.diminuir(p, d)
        print(f'Com o desconto de {d}%, temos {moeda_107.moeda(resultado)}')
    elif r == '3':
        resultado = moeda_107.dobro(p)
        print(f'O dobro de {moeda_107.moeda(p)} é {moeda_107.moeda(resultado)}')
    elif r == '4':
        resultado = moeda_107.metade(p)
        print(f'A metade de {moeda_107.moeda(p)} é {moeda_107.moeda(resultado)}')
    elif r == '0':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.')

    resp = input('\nQuer fazer outra operação? [S/N] ').strip().upper()
    if resp != 'S':
        print('Encerrando...')
        break
