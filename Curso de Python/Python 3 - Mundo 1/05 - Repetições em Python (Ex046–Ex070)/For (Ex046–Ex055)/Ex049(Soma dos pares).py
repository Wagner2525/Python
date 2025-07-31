soma = 0
cont = 0
for i in range(1, 7):
    n = int(input('Digite o {}º numero: '.format(i)))
    if n % 2 == 0:
        cont += 1
        soma += n
 
print('A soma dos {} valores pares é {}'.format(cont, soma))