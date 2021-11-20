"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

tuplanum = (int(input('1º valor: ')),
            int(input('2º valor: ')),
            int(input('3º valor: ')),
            int(input('4º valor: ')))
print('Números digitados:', end=' ')
for n in tuplanum:
    print(n, end=' ')
print(f'\nO nº 9 apareceu {tuplanum.count(9)} vez(es)')
if 3 not in tuplanum:
    print('O nº 3 não apareceu em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {tuplanum.index(3) + 1}ª posição')
print('Valores pares digitados:', end=' ')
for c in tuplanum:
    if c % 2 == 0:
        print(c, end=' ')
