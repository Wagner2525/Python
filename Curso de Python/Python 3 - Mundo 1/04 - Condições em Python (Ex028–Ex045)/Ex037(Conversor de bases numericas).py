num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das base para conversão:
      [1] Converter para BINÁRIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL''')
op = int(input('Sua opção:'))

if op == 1:
    print('[{}] convertido para BINÁRIO é [{}]'.format(num, bin(num)[2:]))
elif op == 2:
    print('[{}] convertido para OCTAL é [{}]'.format(num, oct(num)[2:]))
elif op == 3:
    print('[{}] convertido para HEXADECIMAL é [{}]'.format(num, hex(num)[2:]))
else:
    print("Essa opção não existe!")