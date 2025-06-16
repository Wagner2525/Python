n = 0

while True:
    n = int(input('Quer ver a a taboada de qual valor? '))
    if n < 0:
        break
    for i in range(1, 11):
        m = n * i
        print(f'{n} x {i} = {m}')
