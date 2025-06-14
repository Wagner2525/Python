p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a RAZÃO: '))
t = p
c = 1

while c <= 10:
    print('{} -> '.format(t), end='')
    t += r
    c += 1
print('FIM!!!')
