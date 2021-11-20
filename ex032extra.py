"""Faça um programa que responda o ano atual."""

from datetime import date
ano = str(input('Pressione 0 para saber o ano atual: '))
ano = date.today().year

print(ano)