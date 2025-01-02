import random

a1 = str(input('Digite o primeiro aluno:'))
a2 = str(input('Digite o segundo aluno:'))
a3 = str(input('Digite o terceiro aluno:'))
a4 = str(input('Digite o quarto aluno:'))
a5 = str(input('Digite o quinto aluno:'))

lista = [a1, a2, a3, a4, a5]
sorteado = random.choice(lista)

print('O sorteado foi: {}'.format(sorteado))