"""Crie um programa que faça o computador jogar Jokenpô com você."""

from time import sleep
from random import choice
print('JOKENPÔ!')
user = str(input('Escolha e digite pedra, papel ou tesoura: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.5)
sort = choice(['pedra', 'papel', 'tesoura'])
if user == sort:
    print(f'EMPATE! Escolhemos {sort}.')
elif (user == 'pedra' and sort == 'tesoura') or (user == 'papel' and sort == 'pedra') or (user == 'tesoura' and sort == 'papel'):
    print(f'VOCÊ GANHOU! Escolheu {user} e eu escolhi {sort}.')
else:
    print(f'VOCÊ PERDEU! Escolheu {user} e eu escolhi {sort}.')