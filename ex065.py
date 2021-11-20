"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

cont = 0
soma = 0
again = 'S'
while again != 'N':
    num = int( input( 'Digite um número: ' ) )
    again = str( input( 'Quer continuar? [S/N] ' ) ).strip( ).upper( )[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles é {media}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
