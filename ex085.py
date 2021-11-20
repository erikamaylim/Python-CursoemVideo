"""Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""

todos = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º nº: '))
    if n % 2 == 0:
        todos[0].append(n)
    elif n % 2 != 0:
        todos[1].append(n)
todos[0].sort()
todos[1].sort()
print(f'Valores pares digitados: {todos[0]}')
print(f'Valores ímpares digitados: {todos[1]}')

