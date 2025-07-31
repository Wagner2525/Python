s = 0
c = []
cont = 0

for i in range(1, 11, 2):
    if i % 3 == 0:
        cont += 1
        c.append(i)
        s += i

print('Os números multiplos de 3 e que são ímpares são: {}'.format(c))
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
