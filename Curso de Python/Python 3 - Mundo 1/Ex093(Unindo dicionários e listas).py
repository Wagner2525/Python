pessoa = {}
galera = []
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    while pessoa['sexo'] not in ['M', 'm', 'F', 'f']:
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    resp = str(input('Quer continuar [S/N]? '))
    while resp not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
for pessoa in galera:
    soma += pessoa['idade']
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
média = soma/len(galera)
print(f'B) A média de idade é de {média:5.2f}')
print('C) As mulheres cadastradas foram: ', end='')
for mulher in galera:
    if mulher['sexo'] in 'Ff':
        print(f'{mulher['nome']} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for pessoa in galera:
    if pessoa['idade'] >= média:
        print('  ')
        for chave, valor in pessoa.items():
            print(f'{chave} = {valor}; ', end='')
        print()
print('<< ENCERRADO >>')