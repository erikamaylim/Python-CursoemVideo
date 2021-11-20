"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

num = list()
par = list()
impar = list()
resp = 'S'
while resp in 'Ss':
    num.append(int(input('Digite um nº: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
    else:
        if resp not in 'SsNn':
            resp = str( input( 'Digite apenas S ou N. Quer continuar? ' ) ).strip( )[0]
for v in num:
    if v % 2 == 0:
        par.append(v)
    elif v % 2 != 0:
        impar.append(v)
print(f'Lista com todos os números: {num}')
print(f'Lista com números pares: {par}')
print(f'Lista com números ímpares: {impar}')