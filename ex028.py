'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deve escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
num = randint(0, 5)
aposta = int(input('Estou pensando em um número de 0 a 5. Qual você acha que é? '))
print(f'{aposta}? Será que vc acertou? Hum, vamos ver...')
sleep(3) #Faz uma pausa de n segundos.
print('AÊ, ACERTOU!' if aposta == num else f'ERROU! Eu pensei no {num}, não no {aposta}, zé ruela!')

