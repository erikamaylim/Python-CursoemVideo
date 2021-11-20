"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial."""


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um nº.
    :param num: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :param return: Valor fatorial de um nº num
    """
    if show == False:
        f = 1
        for c in range(num, 0, -1):
            f *= c
    elif show == True:
        f = 1
        for c in range(num, 0, -1):
            print(c, end='')
            print(f' x ' if c > 1 else ' = ', end='')
            f *= c
    return f


print(fatorial(7, True))
