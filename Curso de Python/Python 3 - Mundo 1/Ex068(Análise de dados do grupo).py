c = h = m = 0
print('-'*19)
print('CADASTRE UMA PESSOA')
print('-'*19)
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        c += 1
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            h += 1
            break
        if sexo == 'F':
            if idade < 20:
                m += 1
                break
            break
    flag = str(input('Quer continuar [S/N]? '))
    if flag in 'Ss':
        print('-'*19)
        print('CADASTRE UMA PESSOA')
        print('-'*19)
    if flag in 'Nn':
        break
print('=-'*22)
print(f'Total de pessoas com mais de 18 anos: {c}')
print(f'Ao todo temos {h} homens cadastrados.')
print(f'E temos {m} mulheres com menos de 20 anos.')