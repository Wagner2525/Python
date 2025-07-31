def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa/100)
    if not formato:
        return res
    else:
        return moeda(res)


def diminuir(preço = 0, taxa = 0, formato = False):
    res = preço - (preço * taxa/100)
    if not formato:
        return res
    else:
        return moeda(res)


def dobro(preço = 0, formato = False):
    res = preço * 2
    if not formato:
        return res
    else:
        return moeda(res)


def metade(preço = 0, formato = False):
    res = preço/2
    if not formato:
        return res
    else:
        return moeda(res)


def moeda(preço = 0, moeda = 'R$', formato = False):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço, aumento, redução):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, formato=True)}')
    print(f'Metade do preço: \t{metade(preço, formato=True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, taxa=aumento, formato=True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, taxa=redução, formato=True)}')
    print('-' * 35)