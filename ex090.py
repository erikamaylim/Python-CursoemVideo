"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

aluno = {}
nome = str(input('Nome: '))
aluno['Nome'] = nome
media = float(input(f'Média de {nome}: '))
aluno['Média'] = media
if media >= 7:
    aluno['Situação'] = 'Aprovado(a)'
elif media >= 5:
    aluno['Situação'] = 'Em recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'
print('--' * 20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

