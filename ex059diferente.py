"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
n1 = int(input('Digite o 1º nº: '))
n2 = int(input('Digite o 2º nº: '))
operador = 0
while operador != 5:
    print(f'Para os números {n1} e {n2}:')
    print('''Suas opções:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
    operador = int(input('Digite a opção desejada: '))
    if operador == 1 :
        print( f'{n1} + {n2} = {n1 + n2}' )
    elif operador == 2 :
        print( f'{n1} X {n2} = {n1 * n2}' )
    elif operador == 3 :
        if n1 != n2:
            print( f'Entre {n1} e {n2}, {max(n1, n2)} é o maior.' )
        elif n1 == n2:
            print(f'Os números que digitou são o mesmo, o {n1}.')
    elif operador == 4:
        print('Digite os valores novamente.')
        n1 = int( input( 'Digite o 1º nº: ' ) )
        n2 = int( input( 'Digite o 2º nº: ' ) )
    elif operador == 5:
        print( 'Você saiu do programa.' )
    else:
        print('Opção inválida. Tente novamente.')
    print( '-' * 20 )
    sleep(1)
print('FIM')



