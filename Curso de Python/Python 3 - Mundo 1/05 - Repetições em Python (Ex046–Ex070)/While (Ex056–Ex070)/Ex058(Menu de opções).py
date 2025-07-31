n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0

while op != 5:
    print(''' [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa''')
    op = int(input('Qual a sua opção? '))
    if op == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}.'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('O produto de {} x {} é {}.'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os núemros novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalizando....')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print('Fim do programa!!!')

