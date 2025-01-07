nome = str(input('Digite o seu nome completo: '))

print('Analisando o seu nome...')
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúscula: {}'.format(nome.lower()))
print('Total de letras sem espaços: {}'.format(len(nome.strip())))
print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))