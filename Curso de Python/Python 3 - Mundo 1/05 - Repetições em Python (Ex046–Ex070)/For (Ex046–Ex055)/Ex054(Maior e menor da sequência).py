maior = 0
menor = 0
l = []

for p in range(1, 4):
    peso = float(input('Digite o {}° peso: '.format(p)))
    l.append(peso)
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
l.sort()
print('Todos os pesos digitados (kg): {}'.format(l))        
print('O maior peso foi {}kg e o menor foi {}kg'.format(maior, menor))
