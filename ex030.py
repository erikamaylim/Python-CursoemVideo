"""Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar."""

num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print(f"O número {num} é PAR.")
else:
    print(f'O número {num} é ÍMPAR.')
