n = int(input('Digite um número: '))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print('Foram digitados {} números e a soma foi de {}'. format(cont, soma))
