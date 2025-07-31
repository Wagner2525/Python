frase = str(input('Digite algo para ser analisado: ')).strip().upper()
print('A letra "A" foi aparece {} vezes na frase.'.format(frase.count('A')))
print('A primiera letra "A" apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra "A" está na posição {}'.format(frase.rfind('A') + 1))