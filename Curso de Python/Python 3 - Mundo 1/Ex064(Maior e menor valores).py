'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

c = 'S'
maior = menor = soma = cont = 0
while c == 'S':
    cont += 1
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    soma += n
    media = soma/cont
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Foram digitados {} números.'.format(cont))