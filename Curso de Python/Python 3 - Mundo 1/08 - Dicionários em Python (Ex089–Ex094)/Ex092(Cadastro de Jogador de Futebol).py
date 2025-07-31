j = {}
j['Nome'] =  str(input('Nome do Jogador: '))
j['Gols'] = []
qnt = int(input(f'Quantas partidas {j["Nome"]} jogou? '))
for i in range(0, qnt):
    gol = int(input(f'  Quantos gols na partida {i}? '))
    j['Gols'].append(gol)
soma = sum(j['Gols'])
j['Total'] = soma
print('-=' * 30)
print(j)
print('-=' * 30)
for chave, valor in j.items():
    print(f'O campo |{chave.lower()}| tem valor |{valor}|')
print('-=' * 30)
print(f'O jogador {j["Nome"]} jogou {qnt} partidas')
for i, gols in enumerate(j["Gols"]):
    print(f'    => Na partida {i}, fez {gols}')
print(f'Foi um total de {j['Total']} gols')