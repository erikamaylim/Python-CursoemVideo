"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

num = []
for n in range(1, 6):
    num.append(int(input(f'Digite um nº para a {n}ª posição: ')))
print(f'Números digitados: {num}')
print(f'O MAIOR nº digitado é o {max(num)}, que ocupa a(s) posição(ões): ', end='')
for p, v in enumerate(num):
    if v == max(num):
        print(p + 1, end='; ')
print(f'\nO MENOR nº digitado é o {min(num)}, que ocupa a(s) posição(ões): ', end='')
for p, v in enumerate(num):
    if v == min(num):
        print(p + 1, end='; ')
