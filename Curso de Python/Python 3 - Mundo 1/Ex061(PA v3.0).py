p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a RAZÃO: '))
t = p
c = 1
total = 0
v = 10

while v != 0:
    total += v
    while c <= total:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    v = int(input('Quantos termos você quer mostrar a mais? '))
print('PA finalizada com {} termos mostrados'.format(total))   