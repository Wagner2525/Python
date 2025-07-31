matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = mai = soma_coluna_3 = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}][{j}]: '))
print('-='*30)
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]
    print()
for i in range(0,3):
    soma_coluna_3 += matriz[i][2]
for j in range(0,3):
    if j == 0 or matriz[1][j] > mai:
        mai = matriz[1][j]
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_coluna_3}')
print(f'O mair valor da segnda linha é {mai}')