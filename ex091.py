"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep
jogo = dict()
jogo['Jogador 1'] = randint(1, 6)
jogo['Jogador 2'] = randint(1, 6)
jogo['Jogador 3'] = randint(1, 6)
jogo['Jogador 4'] = randint(1, 6)
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
print()
sleep(1)
print('   ***** RANKING *****')
sleep(1)
'''cont = ''
for i in sorted(jogo, key=jogo.get, reverse=True):
    print(f'Em {cont}º lugar: {i} com {jogo[i]}')
    cont += 1
    sleep(0.5)'''
ranking = sorted(jogo.items(), key=lambda x: x[1], reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)