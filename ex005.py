"""Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor."""
n1 = int(input('Digite um número inteiro: '))
# Poderia ter criado variáveis para antecessor e sucessor, mas só foram usados uma vez no código.
# Seria interessante criar estas variáveis caso precisasse delas novamente no código.
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(n1, n1 - 1, n1 + 1))

