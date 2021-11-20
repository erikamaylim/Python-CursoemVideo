"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”."""

city = str(input('Digite o nome da cidade: ')).strip()
print('A cidade digitada começa com a palavra Santo?', city[0:5].lower() == 'santo')
print('Se a resposta for True, então começa. Se for False, então não começa.')