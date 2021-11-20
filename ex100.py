from random import randint
from time import sleep


def sorteia(lst):
    print(f'Sorteando 5 valores:', end=' ')
    for c in range(5):
        n = randint(1, 10)
        print(n, end=' ')
        sleep(0.4)
        lst.append(n)
    print()


def somaPar(pares):
    soma = 0
    for c in pares:
        if c % 2 == 0:
            soma += c
    sleep(0.5)
    print(f'Somando os valores pares de {pares} temos {soma}.')
    print()


numeros = []
lista = []
sorteia(numeros)
somaPar(numeros)
sorteia(lista)
somaPar(lista)

