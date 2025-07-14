from time import sleep
def maior(* n):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in n:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram digitados {cont} valores.')
    print(f'O maior número digitado foi: {maior}')

#MAIN
maior(9, 3, 4, 5)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()