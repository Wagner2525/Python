lista = []
impar = []
par = []
while True:
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 != 0:
        impar.append(valor)
    lista.append(valor)
    res = str(input('Quer continuar [S/N]? '))
    if res in 'Nn':
        break
print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')