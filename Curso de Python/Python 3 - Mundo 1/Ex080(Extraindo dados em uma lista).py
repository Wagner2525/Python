l = []
while True:
    valor = int(input('Digite um valor:'))
    l.append(valor)
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
ordenado = sorted(l, reverse=True)
print('-=' * 20)
print(f'Você digitou {len(l)} elementos')
print(f'Os valores em ordem decrescente são {ordenado}')
if 5 in l:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')