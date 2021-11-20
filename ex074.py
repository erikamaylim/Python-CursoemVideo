"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla."""

from random import randint
tuplanum = (randint(1, 10), randint(1, 10), randint(1, 10),
            randint(1, 10), randint(1, 10))
print(f'Números sorteados:', end=' ')
for n in tuplanum:
    print(n, end=' ')
print(f'\nMenor nº sorteado: {min(tuplanum)}.')
print(f'Maior nº sorteado: {max(tuplanum)}.')
