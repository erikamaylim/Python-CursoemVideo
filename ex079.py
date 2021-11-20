"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

num = list()
resp = 'S'
while resp in "Ss":
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado. Não vou adicionar.')
    resp = str(input('Quer continuar? [S/N] '))
print('Programa finalizado')
num.sort()
print('Os números digitados em ordem crescente foram:', end=' ')
print(*num, sep=', ')
