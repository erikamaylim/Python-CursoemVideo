"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


from uteis.cores import RED, END


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print(f'{RED}OPS!{END} Você digitou um dado inválido. Tente novamente...')
        else:
            return f


def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'{RED}OPS!{END} Você digitou um dado inválido. Tente novamente...')
        else:
            return i


n1 = leiaFloat('Digite um nº real: ')
n2 = leiaInt('Digite um nº inteiro: ')
print(f'Você digitou o nº real {n1} e o nº inteiro {n2}.')

