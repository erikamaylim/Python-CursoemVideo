"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

n = int(input('Digite um nº [999 para parar]: '))
c, s = 0, 0
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um nº [999 para parar]: '))
print(f'Você digitou {c} números. A soma deles é {s}.')
