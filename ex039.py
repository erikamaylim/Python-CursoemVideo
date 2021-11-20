"""Faça um programa que leia o ano de nascimento de um jovem e informe,
e acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
print('***** ALISTAMENTO MILITAR *****')
ano = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - ano
if idade < 18:
    print(f'Você ainda não tem 18 anos e ainda vai se alistar ao serviço militar em {ano + 18}. Falta(m) {18 - idade} anos.' )
elif idade == 18:
    print(f'Você tem 18 anos e deve se alistar às forças armadas imediatamente.')
elif idade > 18:
    print(f'''Você tem mais de 18 anos. Seu ano de alistamente ao serviço militar foi {ano + 18}, à {idade - 18} ano(s).''')
print('FIM')






