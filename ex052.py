"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num + 1, 1):
    if num % c == 0:
        print('\033[1;32m', end=' ')
        cont += 1
    else:
        print('\033[1;31m', end=' ')
    print(c, end=' ')
print('\n\033[m', f'O número {num} é divisível {cont} vezes.')
if cont == 2:
    print(f'Portanto, {num} É UM NÚMERO PRIMO!')
else:
    print(f'Portanto, {num} NÃO É PRIMO!')

