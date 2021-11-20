"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

si = float(input('Digite seu salário atual: R$ '))
sf = si + (si * 15 / 100)
print('Seu novo salário com 15% de aumento é R$ {:.2f}.'.format(sf))
