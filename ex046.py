"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

from emoji import emojize
from time import sleep
for c in range (10, -1, -1):
    print(c)
    sleep(0.3)
print(emojize(":fireworks:"))