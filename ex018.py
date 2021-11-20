"""Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo."""

from math import sin, cos, tan, radians
x = float(input('Digite o valor de um ângulo: '))
s = sin(radians(x))
c = cos(radians(x))
t = tan(radians(x))
print(f'O ângulo digitado foi {x}. Seu seno é {s:.2f}, seu cosseno é {c:.2f} e a sua tangente é {t:.2f}')

#x = int(input('Digite um grau qualquer:' ))
#print(f'O ângulo digitado foi {x}. Seu seno é {sin(x)}, seu cosseno é {cos(x)} e a sua tangente é {tan(x)}.')
