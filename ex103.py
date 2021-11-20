"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar
a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""


def ficha(nome='', gols=''):
    if nome == '' or nome.isnumeric():
        nome = "<desconhecido>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s).')


n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Nº de gols: '))
ficha(n, g)
