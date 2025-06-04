from datetime import date
ano = int(input('Ano de nasciemnto:'))
ano_atual = date.today().year
idade_min = 18
calc_idade = ano_atual - ano  

print('Você nasceu em {} e tem {} anos em {}'.format(ano, calc_idade, ano_atual))

if calc_idade < idade_min:
    print('Ainda faltam {} anos para o alistamento!'.format(idade_min - calc_idade))
    print('Seu alistamento será em {}.'.format((idade_min - calc_idade) + ano_atual))
elif calc_idade > idade_min:
    print('Você já deveria ter se alistado há {} anos!'.format(calc_idade - idade_min))
    print('Seu alistamneto foi em {}...'.format(ano + idade_min))
elif calc_idade == idade_min:
    print('Trate de se alistar IMEDIATAMENTE, pequeno jovem!')
else:
    print('Alistamento feito com sucesso!!')
