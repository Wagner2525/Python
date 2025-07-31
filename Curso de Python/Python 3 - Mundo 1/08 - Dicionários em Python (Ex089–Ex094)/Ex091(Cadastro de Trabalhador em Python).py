from datetime import date

trabalhador = {}
ano_atual = date.today().year

trabalhador['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = ano_atual - nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))

if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['contratacao'] + 35 - nasc

print('-=' * 30)
for k, v in trabalhador.items():
    print(f'{k}: {v}')
