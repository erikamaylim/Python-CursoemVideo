"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

n1 = int(input('Digite o 1º nº: '))
n2 = int(input('Digite o 2º nº: '))
print('''Suas opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa ''')
operador = int(input('Digite a opção desejada: '))
while operador == 4:
    n1 = int( input( 'Digite o 1º nº: ' ) )
    n2 = int( input( 'Digite o 2º nº: ' ) )
    print( '''Suas opções:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa ''' )
    operador = int( input( 'Digite a opção desejada: ' ) )
if operador == 1:
    print(f'{n1} + {n2} = {n1 + n2}')
elif operador == 2:
    print(f'{n1} X {n2} = {n1 * n2}')
elif operador == 3:
    if n1 > n2:
        print(f'O primeiro nº digitado, {n1}, é MAIOR que o segundo, {n2}.')
    elif n1 < n2:
        print(f'O segundo nº digitado, {n2}, é MAIOR que o primeiro, {n1}.')
    elif n1 == n2:
        print(f'Você digitou duas vezes o número {n1}. Portanto, digitou números iguais.')
elif operador == 5:
    print('Você saiu do programa.')
print('FIM')