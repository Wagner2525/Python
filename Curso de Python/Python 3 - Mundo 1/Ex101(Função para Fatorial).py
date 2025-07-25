def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for i in range(n, 0, -1):   
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f          
    
# Main
print(f'Primeira forma de rodar: {fatorial(5)}')
print('Segunda forma de rodar: ', end='')
print(fatorial(5, show=True))
help(fatorial)