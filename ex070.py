"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

maisdemil = barato = total = produtos = 0
maisbarato = ' '
continuar = 'S'
while True:
    nome = str( input( 'Nome do produto: ' ) ).strip( )
    preco = float( input( 'Preço do produto: R$ ' ) )
    produtos += 1
    total += preco
    if preco > 1000:
        maisdemil += 1
    if produtos == 1 or preco < barato:
        barato = preco
        maisbarato = nome
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str( input( 'Quer continuar? ' ) ).strip( )[0]
    if continuar in 'Nn':
        print('=-' * 15)
        print('COMPRA FINALIZADA')
        print('=-' * 15)
        break
print(f'Total da compra: R$ {total:.2f}.')
print(f'Qntd de produtos com valor acima de R$ 1000.00: {maisdemil}.')
print(f'Produto mais barato: {maisbarato}, de R$ {barato:.2f}.')


