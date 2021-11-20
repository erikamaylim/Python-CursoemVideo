"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Você tem {idade} anos e pertence à categoria MIRIM (até 9 anos).')
elif idade <= 14:
    print(f'Você tem {idade} anos e pertence à categoria INFANTIL (10 a 14 anos).')
elif idade <= 19:
    print(f'Você tem {idade} anos e pertence à categoria JUNIOR (15 a 19 anos).')
elif idade <= 25:
    print(f'Você tem {idade} anos e pertence à categoria SENIOR (20 a 25 anos).')
else:
    print(f'Você tem {idade} anos e pertence à categoria MASTER (acima de 25 anos).')