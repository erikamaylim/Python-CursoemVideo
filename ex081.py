"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

num = list()
resp = 'S'
while True:
    if resp in 'Ss':
        num.append(int(input('Digite um nº: ')))
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    elif resp in 'Nn':
        break
    else:
        while resp not in 'Ss' and resp not in 'Nn':
            resp = str(input('Digite apenas S ou N. Quer continuar? ')).strip()[0]
num.sort()
num.reverse()
print('-' * 30)
print(f'Foram digitados {len(num)} números.')
print('-' * 30)
print(f'A lista em ordem decrescente é: {num}')
print('-' * 30)
if 5 in num:
    print('O nº 5 está na lista.')
else:
    print('O nº 5 NÃO está na lista.')
