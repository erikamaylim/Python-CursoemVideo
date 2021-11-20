"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""

from math import hypot
x = float(input('Digite o comprimento do cateto oposto: '))
y = float(input('Digite o comprimento do cateto adjacente: '))
print(f'Quando cateto oposto é {x:.2f} e cateto adjacente é {y:.2f}, a hipotenusa é {hypot(x,y):.2f}')
