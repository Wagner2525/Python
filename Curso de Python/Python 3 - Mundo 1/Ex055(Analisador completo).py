soma = 0
maior = 0
cont = 0
nome_mais_velhor = ''

for i in range(1, 5):
    print('===== {}º PESSOA ====='.format(i))
    nome = str(input('\033[34mNome: \033[0m')).strip()
    idade = int(input('\033[34mIdade: \033[0m'))
    sexo = str(input('\033[34mSexo [M/F]: \033[0m')).strip()
    soma += idade

    if   i == 1 and sexo in 'Mm':
        maior = idade
        nome_mais_velhor = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nome_mais_velhor = nome
    if sexo in 'Ff':
        if idade < 20:
            cont += 1
media = soma/i

print('A média de idade do grupo é de \033[31m{}\033[0m anos'.format(media))
print('O homem mais velho tem \033[31m{}\033[0m anos e se chama \033[31m{}\033[0m'.format(maior, nome_mais_velhor))
print('Ao todo são \033[31m{}\033[0m mulheres com menos de 20 anos'.format(cont))