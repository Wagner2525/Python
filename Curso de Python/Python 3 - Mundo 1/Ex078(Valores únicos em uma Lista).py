l = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in l:
        l.append(valor)
        print('Valor add com sucesso!')
    else:
        print('Esse valor já está na lista e não será add!!')
    flag = str(input('Quer continuar [S/N]? '))
    if flag in 'Nn':
        break
print('-='*15)
print(f'Você digitou os valores {l}')