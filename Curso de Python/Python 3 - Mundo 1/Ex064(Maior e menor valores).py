c = 'S'
maior = menor = soma = cont = 0
while c == 'S':
    cont += 1
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    soma += n
    media = soma/cont
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Foram digitados {} números.'.format(cont))