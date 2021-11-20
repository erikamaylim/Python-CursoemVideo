"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

"""num = int(input('Digite um número para exibir os 10 primeiros termos de sua PA: '))
razao = int(input('Defina a razão da sua PA: '))
for c in range(num, num + (11 - 1) * razao, razao):
    print(c, end=' ')"""

cont = 1
num = int(input('Digite um número para exibir os 10 primeiros termos de sua PA: '))
razao = int(input('Defina a razão da sua PA: '))
while cont <= 10:
    print(num, '⇾', end=' ')
    num += razao
    cont += 1
print('FIM')