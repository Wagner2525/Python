lista = [[], []]
valor = 0
for i in range(1,8):
    valor = int(input(f'Digite o {i} valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 != 0:
        lista[1].append(valor)
lista[0].sort
lista[1].sort
print('-='*30)
print(f'Lista digitada foi: {lista}')
print(f'Os valores pares pares digitados foram: {lista[0]}')
print(f'Os valores pares ímpares digitados foram: {lista[1]}')