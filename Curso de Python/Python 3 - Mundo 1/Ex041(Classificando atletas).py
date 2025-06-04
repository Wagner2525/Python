from datetime import date

ano = int(input('Ano de nascimento:'))
ano_atual = date.today().year
idade = ano_atual - ano

print('=======CLASSICAÇÃO=======')
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Júnior')
elif  idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
