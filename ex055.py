"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

'''lista = []
for p in range(1,6):
    peso = float(input(f'Digite o {p}º peso: '))
    lista.append(peso)
print(f'O maior peso é {max(lista)}Kg.')
print(f'O menor peso é {min(lista)}Kg.')'''

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}Kg e o menor é {menor}Kg.')



