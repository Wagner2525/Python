ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('-='*13)
print(f'{'No.':<4}{'Nome':<10}{'Média':>8}')
print('-'*26)
for i, valor in enumerate(ficha):
    print(f'{i:<4}{valor[0]:<10}{valor[2]:>8}')
while True:
    print('-' * 30)
    opc = int(input('Mosttrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são: {ficha[opc][1]}')