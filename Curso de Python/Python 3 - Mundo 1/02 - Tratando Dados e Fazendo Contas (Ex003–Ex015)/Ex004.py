n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))

s = n1 + n2 #soma
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 #div inteira
e = n1 ** n2 #potência
r = n1 % n2 #resto da div

# end=' ' => juntar dois prints

print('A soma é {}, o produto é {} e a divisão é {:.2}'.format(s, m, d))
print('A divisão inteira é {}, a potência é {} e o resto da divisão é {}'.format(di, e, r))