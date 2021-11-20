"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

galera = []
dados = []
peso = []
resp = 'S'
while resp in 'Ss':
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
    elif resp not in 'SsNn':
        resp = str(input('Inválido. Responda com S ou N. Quer continuar? [S/N] ')).strip()[0]
print('--' * 20)
print(f'{len(galera)} pessoas foram cadastradas.')
for n, p in galera:
    peso.append(p)
print(f'Maior peso registrado foi {max(peso)}Kg de ', end='')
for n, p in galera:
    if p == max(peso):
        print(f'[{n}]', end=' ')
print(f'\nMenor peso registrado foi {min(peso)}Kg de ', end='')
for n, p in galera:
    if p == min(peso):
        print(f'[{n}]', end=' ')
