print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif a != b != c != a:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
else:
    print('Com os segmentos acima NÃO se pode formar um triângulo! :/')