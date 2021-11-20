"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira."""

from math import trunc
n = float(input('Digite um número real: '))
print(f'O número {n} tem a parte inteira {trunc(n)}')

'''Outra forma de fazer:
n = float(input('Digite um número real: '))
print(f'O número {n} tem a parte inteira {int(n)}.')'''