print('=' * 30)
print(f'{'LISTAGEM DE PREÇOS':^30}')
print('=' * 30)
lista = ('Lápis', 1.2, 'Borracha', 0.5, 'Caneta', 1.5,'Grafite', 2, 'Estojo', 9.99, 'Caderno', 20, 'Mochila', 150, 'Lancheira', 49.99)

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>7.2f}')
