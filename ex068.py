"""Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint
c = 0
print('******** PAR OU ÍMPAR ********')
print(' ')
while True:
    num = int( input( 'Escolha um número de 1 a 5: ' ) )
    pc = randint(1, 5)
    soma = num + pc
    opcao = ' '
    while opcao not in 'PpIi':
        opcao = str( input( 'Par ou ímpar [P/I]: ' ) ).strip( )[0]
    print(f'Você jogou: {num}. Computador jogou: {pc}.')
    if soma % 2 == 0:
        print(f'{soma} é par')
        if opcao in 'Pp':
            print('GANHOU!')
            c += 1
        else:
            print('PERDEU!')
            print( '=-' * 10 )
            break
    if soma % 2 != 0:
        print(f'{soma} é ímpar.')
        if opcao in "Ii":
            print('GANHOU!')
            c += 1
        else:
            print('PERDEU!')
            print( '=-' * 10 )
            break
print(f'GAME OVER! Você venceu {c} vez(es).')
