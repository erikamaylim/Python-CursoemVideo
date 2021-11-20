"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
maiores = 0
menores = 0
for c in range(1, 8):
    n = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if date.today().year - n >= 21:
        maiores += 1
    elif date.today().year - n < 21:
        menores += 1
print(f'{maiores} pessoas já atingiram a maioridade.')
print(f'{menores} pessoas ainda não atingiram a maioridade.')
