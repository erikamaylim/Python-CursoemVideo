"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Com as medidas {r1}, {r2} e {r3}, SIM, é possível formar um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO. Todos os lados são iguais.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triângulo é ISÓSCELES. Possui 2 lados iguais.')
    elif r1 != r2 and r2 != r3 and r3 != r1: #Ou r1 != r2 != r3 != r1
        print('O triângulo é ESCALENO. Possui todos os lados diferentes.')
else:
    print(f'Com as medidas {r1}, {r2} e {r3} NÃO é possível formar um triângulo.')
