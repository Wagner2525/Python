n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',  'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {n[num]}')
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
         print('Número inválido. Tente novamente. ', end= '')