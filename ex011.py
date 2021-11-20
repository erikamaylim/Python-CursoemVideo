"""Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

l = float(input('Digite a largura em metros: '))
h = float(input('Digite a altura em metros: '))
a = l * h
t = a / 2
print('A área tem {:.2f}m² e são necessários {:.2f} litros de tinta.'.format(a, t))
