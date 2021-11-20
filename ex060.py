"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""

m = 1
n = int(input('Digite um nº e encontre seu fatorial: '))
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    m = m * c
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
print(f'{m}', end='')

'''from math import factorial
n = int(input('Digite um nº e encontre seu fatorial: '))
print(factorial(n))'''