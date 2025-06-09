from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0
tds_as_idades = []

for i in range(1, 8):
    nascimento = int(input('Em que ano nasceu a {} pessoa: '.format(i)))
    idade = ano_atual - nascimento
    tds_as_idades.append(idade)
    if idade > 18:
        maior += 1
    else:
        menor += 1
        
tds_as_idades.sort() 
print('Todas as idades: {}'.format(tds_as_idades))
print('{} pessoas são maiores de idade e {} são menores!'.format(maior, menor))
