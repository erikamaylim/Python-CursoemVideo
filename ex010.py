"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar."""

d = float(input('Quantos Reais você tem? R$ '))
print('Com R$ {:.2f} você pode comprar US$ {:.2f}.'.format(d, d / 3.27))
print(f'Com R$ {d:.2f} você pode comprar US$ {d/3.27:.2f}.')
