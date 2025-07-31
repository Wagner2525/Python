def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno é {largura} x {comprimento} é de {a}m²')

print('=' * 30)
print(f'{'Área do terreno':^30}')
print('=' * 30)
l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))
área(l, c)
