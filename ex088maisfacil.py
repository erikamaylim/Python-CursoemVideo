"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import sample
from time import sleep
for n in range(int(input("Nº de jogos: "))):
    print(f'Jogo {n + 1}:', end=' ')
    print(sorted(sample(range(1, 61), 6)))
    sleep(0.7)
