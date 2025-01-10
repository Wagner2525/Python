n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

print('Os valores digitados foram: {}, {} e {}.'.format(n1, n2, n3))
if n1 > n2 and n1 > n3:
    print("O maior valor é: {}".format(n1))
elif n2 > n1 and n2 > n3:
    print("O maior valor é: {}".format(n2))
else:
    print('O maior valor é: {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor valor é: {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor valor é: {}'.format(n2))
else:
    print('O menor valor é: {}'.format(n3))