"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""

m = 1
n = int(input('Digite um nº e encontre seu fatorial: '))
c = n
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' X ' if c > 1 else ' = ', end='')
    m *= c
    c -= 1
print(m)



