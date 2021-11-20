"""Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um número inteiro para conversão: '))
conv = int(input('''Qual a base para conversão?
1 para binário
2 para octal
3 para hexadecimal
Digite sua opção: '''))
RED = "\033[1;31m"
END = "\033[0m"
GREEN = "\033[1;32m"
if conv == 1:
    print(f'{num} em binário é {GREEN}{format(num, "b")}{END}')
elif conv == 2:
    print(f'{num} em octal é {GREEN}{format(num, "o")}{END}')
elif conv == 3:
    print(f'{num} em hexadecimal é {GREEN}{format(num, "X")}{END}')
else:
    print(f'{RED}Opção inválida{END}')
print('FIM')

"""Site com explicação de como fazer conversão: https://www.delftstack.com/pt/howto/python/python-int-to-binary/#:~:text=bin%C3%A1rio%20em%20Python.-,Utilize%20bin()%20Fun%C3%A7%C3%A3o%20para%20Converter%20Int%20para%20Bin%C3%A1rio%20em,bin%C3%A1ria%20equivalente%20prefixada%20com%200b%20."""