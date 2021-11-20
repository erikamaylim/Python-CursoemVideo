"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 16 <= idade <= 17 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade <= 15:
        return f'Com {idade} anos: NÃO VOTA'


print(voto(int(input('Ano de nascimento: '))))

