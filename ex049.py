"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for."""

n = int(input('Digite um número inteiro para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} X {c:2} = {(n * c):3}')
