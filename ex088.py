"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep
todosjogos = []
jogo = []
quant = int(input('Nº de jogos: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    todosjogos.append(jogo[:])
    jogo.clear()
    total += 1
for i, l in enumerate(todosjogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)

