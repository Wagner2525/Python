n = int(input('Digite um número: '))
cont = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\nO número {} fi divisível {} vezes'.format(n, cont))