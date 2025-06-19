p = t = ()
nove = 0
for i in range(0, 4):
    num = int(input('Digite um valor: '))
    t += (num,)
    if num == 9:
        nove += 1
    if num % 2 == 0:
        par += (num,)
print(f'Os valores que vc digitou foram: {t}')
print(f'O valor 9 apareceu {nove} vezes')
print(f'O valor 3 apareceu na {t.index(3)+1}º posição')
print(f'Os valor par digitado foi: {par}')