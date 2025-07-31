salario = float(input('Digite o seu salário: R$'))
print('Seu salário é: R${:.2f}'.format(salario))

if salario > 1250.00:
    aumento = salario * 1.1
    print('Sei salário teve um aumento de 10% e passou a ser R${:.2f}'.format(aumento))
else:
    aumento = salario * 1.15
    print('Seu salário teve um aumento de 15% e passou a ser R${:.2f}'.format(aumento))