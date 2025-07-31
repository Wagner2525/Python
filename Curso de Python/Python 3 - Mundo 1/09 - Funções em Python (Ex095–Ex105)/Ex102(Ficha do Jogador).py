def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} no campeonato.')

print('-' * 30)
nome = str(input('Nome do Jogador: '))
n_gols = str(input('Número de Gols: '))

if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0
if nome.strip() == '':
    ficha(gol=n_gols)
else:
    ficha(nome, n_gols)