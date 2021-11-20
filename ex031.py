"""Desenvolva um programa que pergunte a distância de uma viagem em quilômetros.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km
e R$ 0,45 para viagens mais longas."""

dist = float(input('Quantos quilômetros de distância a viagem tem? '))
if dist <= 200:
    print(f'O valor da passagem é R${int(dist) * 0.50:.2f}.')
else:
    print(f'O valor da passagem é R${int(dist) * 0.45:.2f}.')