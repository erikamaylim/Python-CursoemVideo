"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date
worker = dict()
worker['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
worker['Idade'] = idade
ctps = int(input('Nº da CTPS (0 se não tiver): '))
worker['CTPS'] = ctps
if worker['CTPS'] != 0:
    anocontrat = int( input( 'Ano de contratação: ' ) )
    worker['Ano de Contratação'] = anocontrat
    worker['Salário'] = float( input( 'Salário: R$ ' ) )
    aposent = (anocontrat + 35) - nasc
    worker['Idade para aposentar'] = aposent
for k, v in worker.items():
    print(f'{k} tem valor {v}.')

'''for i in worker.items():
    if worker['CTPS'] == 0:
        break
    else:
        anocontrat = int( input( 'Ano de contratação: '))
        worker['Ano de Contratação'] = anocontrat
        worker['Salário'] = float( input( 'Salário: R$ '))
        aposent = (anocontrat + 35) - nasc
        worker['Idade para aposentar'] = aposent
        break
print(worker)
for k, v in worker.items():
    print(f'{k} tem valor {v}.')'''

