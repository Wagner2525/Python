pessoa = []
grupo = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa [1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Os dados foram: {grupo}')
if len(grupo) == 1:
    print(f'{len(grupo)} pessoa foi cadastrada!')
else:
    print(f'{len(grupo)} pessoas foram cadastradas!')
print(f'O maior peso foi de {maior}kg. Nome da pessoa: ', end='')
for peso in grupo:
    if peso[1] == maior:
        print(f'[{peso[0]}]', end='')
print()
print(f'O menor peso foi de {menor}kg. Nome da pessoa: ', end='')
for peso in grupo:
    if peso [1] == menor:
        print(f'[{peso[0]}]', end='')