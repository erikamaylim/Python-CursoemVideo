"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos pretende pagar o valor total? '))
mes = anos * 12
prestacao = casa / mes
GREEN = "\033[1;32m"
RED = "\033[1;31m"
END = "\033[0m"
if prestacao <= salario * (30 / 100):
    print(f'{GREEN}EMPRÉSTIMO APROVADO!{END} Você irá pagar R$ {prestacao:.2f} por mês.')
else:
    print(f'{RED}EMPRÉSTIMO NEGADO!{END} O valor das prestações excedeu 30% do seu salário.')
