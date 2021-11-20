"""Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

lista = []
dicionario = {}
somaidades = 0
while True:
    dicionario['Nome'] = str(input('Nome: ')).strip().title()
    dicionario['Sexo'] = str(input('Sexo [M/F]: ')).strip()[0].upper()
    if dicionario['Sexo'] not in 'MmFf':
        dicionario['Sexo'] = str(input('OPÇÃO INVÁLIDA. Apenas M ou F. \nSexo [M/F]: ')).strip()[0].upper()
    dicionario['Idade'] = int(input('Idade: '))
    somaidades += dicionario['Idade']
    lista.append(dicionario.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp not in 'SsNn':
        resp = (str(input('OPÇÃO INVÁLIDA. Apenas S ou N.\nQuer continuar? [S/N]: '))).strip()[0]
    elif resp in 'Nn':
        break
print()
print('=-' * 30)
print(f'Total de pessoas cadastradas: {len(lista)}')
print()
mediaidade = somaidades / len(lista)
print(f'Média de idade do grupo: {mediaidade}')
print()
print(f'Mulheres cadastradas:', end=' ')
for p in lista:
    if p['Sexo'] in 'Ff':
        print(f'[{p["Nome"]}]', end=' ')
print()
print()
print('Pessoas com idade acima da média: ')
for p in lista:
    if p['Idade'] > mediaidade:
        print(f' > {p["Nome"]}, sexo {p["Sexo"]}, {p["Idade"]} anos')
print('=-' * 30)
