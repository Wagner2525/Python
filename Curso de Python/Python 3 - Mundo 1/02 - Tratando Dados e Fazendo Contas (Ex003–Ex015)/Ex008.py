n = float(input('Digite o valor em metros para ser convertido:'))

cm = n * 100
mm = n * 1000

print('Valor em metros {}\nEm centímetros: {:.0f}\nEm milímetros: {:.0f}'.format(n, cm, mm))