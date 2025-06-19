from random import randint

n = (randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15))
ordenado = tuple(sorted(n))
print(f'Os números sorteados foram: {n}')
print(f'O maior número foi: {max(n)}')
print(f'O menor número foi: {min(n)}')
