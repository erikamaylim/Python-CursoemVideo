"""Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""


def calcarea(l, c):
    m = l * c
    print(f'A área de um terreno {l} x {c} é de {m}m².')


def titulo(txt):
    print(f"---  {txt}  ---".upper())


titulo('controle de terrenos')
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
calcarea(larg, comp)
