"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

km = float(input('Digite quantos quilômetros foram percorridos: '))
d = float(input('Digite a quantidade de dias que o carro ficou alugado: '))
p = (60 * d) + (0.15 * km)
print(f'Para {km:.2f}Km rodados e {d:.0f} dias de uso, o valor a pagar é de R${p:.2f}.')
