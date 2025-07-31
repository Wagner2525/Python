t = ()
nove = 0

for i in range(4):
    num = int(input('Digite um valor: '))
    t += (num,)
    if num == 9:
        nove += 1

print(f'\nOs valores que você digitou foram: {t}')
print(f'O valor 9 apareceu {nove} vezes')

if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares digitados foram: ', end='')
for n in t:
    if n % 2 == 0:
        print(n, end=' ')
