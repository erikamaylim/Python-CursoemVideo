"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se els podem ou não
formar um triângulo."""

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Com as medidas {r1}, {r2} e {r3}, SIM, é possível formar um triângulo.')
else:
    print(f'Com as medidas {r1}, {r2} e {r3} NÃO é possível formar um triângulo.')
