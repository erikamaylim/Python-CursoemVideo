"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500."""

'''s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print(f'A soma de todos os múltiplos de 3 no intervalo de 1 a 500 é {s}.')'''

s = 0
cont = 0
for n in range(3, 500, 2):
    if n % 3 == 0:
        cont += 1
        s += n
print(f'A soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500 é {s}. Total de {cont} ímpares múltiplos de 3.')
