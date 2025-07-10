aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] =  float(input('Média: '))
print('-=' * 30)
print(f'- nome é igual a {aluno['Nome']}')
print(f'- média é igual a {aluno['Média']}')
if aluno['Média'] >= 7:
    print('- situação é igual a Aprovado')
elif 5 <= aluno['Média'] < 7:
    print('- situação é igual a Recuperação')
else:
    print('- situação é igual a Reprovado')
