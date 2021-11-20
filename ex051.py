"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

primeiro = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
decimo = primeiro + (11 - 1) * razao              # an = a1 + (n – 1) . r / 11 pq o range ignora o último termo.
for c in range (primeiro, decimo, razao):
    print(c, end= " -> ")
print('FIM')

