"""Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit."""

c = float(input('Digite a temperatura em graus Celsius: '))
print(f'A temperatura de {c:.1f}ºC convertida para Fahrenheit é igual a {(c * (9/5)) + 32:.1f}ºF.')