"""Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez
e em que posição ela aparece a última vez."""

p = str(input('Digite uma frase qualquer: ')).strip().lower()
print(f'Na frase {p} a letra A aparece {p.count("a")} vezes.')
print('A primeira letra A aparece na posição', p.find('a') + 1)
print('A última letra A aparece na posição', p.rfind('a') + 1)
