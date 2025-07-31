palavras = (
    'cachorro', 'gato', 'livro', 'janela', 'mesa',
    'cadeira', 'telefone', 'computador', 'carro', 'estrada',
    'chave', 'porta', 'papel', 'caneta', 'prato'
)

for i in palavras:
    print(f'\nNa palavra \033[31m{i.upper()}\033[0m temos de vogais: ', end='')

    vogais = ()
    for letra in i:
        if letra.lower() in 'aeiou':
            vogais += (letra,)
    for j in range(len(vogais)):
        if j == len(vogais) - 1:
            print(vogais[j] + '.', end=' ')
        else:
            print(vogais[j] + ',', end=' ')