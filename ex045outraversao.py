"""Crie um programa que faça o computador jogar Jokenpô com você."""

from time import sleep
from random import randint
print('######### JOKENPÔ #########')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
user = int(input('Digite o nº da sua opção: '))
lista = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.5)
if user == comp:
    print(F'EMPATE! Escolhemos {lista[comp]}.')
elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
    print(f'VOCÊ GANHOU! Escolheu {lista[user]} e eu escolhi {lista[comp]}.')
elif (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
    print(f'VOCÊ PERDEU! Escolheu {lista[user]} e eu escolhi {lista[comp]}.')
else:
    print('Opção inválida! Tente de novo.')


