"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso."""

tuplanum = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = 'S'
while True:
    num = int(input('Digite um número de 1 a 20: '))
    if num in range(1, 21):
        continuar = str(input(f'Você digitou o nº {tuplanum[num - 1]}. Quer continuar? [S/N] ')).strip()[0]
        if continuar in 'Nn':
            break
    else:
        print('Tente novamente. ', end='')
print('Programa finalizado.')