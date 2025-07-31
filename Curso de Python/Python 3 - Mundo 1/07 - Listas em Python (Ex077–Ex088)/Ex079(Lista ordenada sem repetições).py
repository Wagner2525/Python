l = []
for c in range(1,6):
    valor = int(input('Digite um valor: '))
    if c == 1 or valor > l[-1]:
        l.append(valor)
        print('Foi add ao final da lista...')
    else:
        pos = 0
        while pos < len(l):
            if valor <= l[pos]:
                l.insert(pos, valor)
                print(f'Foi add na posição {pos} da lista...')
                break
            pos += 1
print(f'A lista ficou assim: {l}')
