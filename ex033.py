"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite outro número inteiro qualquer: '))
n3 = int(input('Digite mais um número inteiro qualquer: '))

if n1 > n2  and n1 > n3:
    print(f'Maior número digitado é {n1}.')
if n2 > n1  and n2 > n3:
    print(f'Maior número digitado é {n2}.')
if n3 > n1  and n3 > n2:
    print(f'Maior número digitado é {n3}.')

if n1 < n2  and n1 < n3:
    print(f'Menor número digitado é {n1}.')
if n2 < n1  and n2 < n3:
    print(f'Menor número digitado é {n2}.')
if n3 < n1  and n3 < n2:
    print(f'Menor número digitado é {n3}.')
