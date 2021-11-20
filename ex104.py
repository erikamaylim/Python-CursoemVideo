"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)"""
from uteis.cores import RED, END


def leiaInt(msg):
    RED = "\033[1;31m"
    END = "\033[0m"
    n = str(input(msg)).strip()
    if n.isnumeric():
        n = int(n)
    else:
        while not n.isnumeric():
            n = str(input(f'{RED}ERRO! Digite um número inteiro: {END}')).strip()
            if n.isnumeric():
                break
    return n


n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou {n}.')