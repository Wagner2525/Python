l = []
maior = menor = 0
for c in range(0, 6):
    l.append(int(input(f'Digite um valor para posição {c}:')))
    if c == 0:
        maior = menor = l[c] 
    else:
        if l[c] > maior:
            maior = l[c] 
        if l[c] < menor:
            menor = l[c]
print('=-'*30)
print(f'A lista foi: {l}') 
print(f'O maior foi {maior}, e foi achado na posição ', end='')
for i, j in enumerate(l):
    if j == maior:
        print(f'{i}...', end='')
print(f'\nO menor foi {menor}, e foi achado na posição ', end='')
for i, j in enumerate(l):
    if j == menor:
        print(f'{i}...', end='')
    