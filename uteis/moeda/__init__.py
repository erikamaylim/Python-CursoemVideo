def dobro(v, f=False):
    res = v * 2
    if not f:
        return f'R$ {res}'
    else:
        return dinheiro(res)


def metade(v, f=False):
    res = v / 2
    if not f:
        return f'R$ {res}'
    else:
        return dinheiro(res)


def aumentar(v, f=False):
    res = v + (v * (10 / 100))
    if not f:
        return f'R$ {res}'
    else:
        return dinheiro(res)


def diminuir(v, f=False):
    res = v - (v * (13 / 100))
    if not f:
        return f'R$ {res}'
    else:
        return dinheiro(res)


def dinheiro(v):
    return f'R$ {v:.2f}'.replace('.', ',')


def resumo(v):
    print(f'-' * 30)
    print('RESUMO DO VALOR'.center(28))
    print(f'-' * 30)
    print(f'Preço analisado: \t{dinheiro(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'10% de aumento: \t{aumentar(v, True)}')
    print(f'13% de redução: \t{diminuir(v, True)}')





