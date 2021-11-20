"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

n = int(input('Digite um número até 9999: '))
n = '000' + str(n)
print(f'Unidade = {n[-1]}')
print(f'Dezena = {n[-2]}')
print(f'Centena = {n[-3]}')
print(f'Milhar = {n[-4]}')
