"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”."""

city = str(input('Digite o nome de uma cidade: '))
min = city.lower()
dividido = min.split()
print('O nome da cidade começa com a palavra SANTO?', dividido[0] == 'santo')
print('Se a resposta for True, então começa. Se for False, então não.')
