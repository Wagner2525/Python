v = int(input('Digite a sua velocidade: '))

if v > 80:
    multa = (v - 80) * 7
    print('Você foi multado por ultrapassar a velocidade de 80km/h. \nSua multa foi R${}'.format(multa))
else:
    print('Está tudo ok! Liberado!')