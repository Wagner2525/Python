p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a RAZÃO: '))
d = p + (10 - 1) * r

for i in range(p, d + r, r):
    print('{}'.format(i), end=' -> ')
print('FIM!')