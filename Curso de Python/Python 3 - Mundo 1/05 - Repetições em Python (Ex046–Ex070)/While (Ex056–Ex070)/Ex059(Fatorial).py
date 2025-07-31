n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('CALCULANDO: {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))