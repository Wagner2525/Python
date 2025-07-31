peso = float(input('Digite o seu peso (Kg):'))
altura = float(input('Digite a sua altura (m):'))
imc = peso/(altura**2)

print('Seu IMC é de {:.1f}!'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso!')
elif imc <= 25:
    print('Peso Ideal!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade Mórbida')