"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o4/ aumento é de 15%"""

sal = float(input('Informe seu salário atual para calcularmos o seu novo salário: R$ '))
if sal <= 1250:
    print(f'Seu salário com reajuste de 15% é R$ {sal + (sal * (15 / 100))}')
else:
    print(f'Seu salário com reajuste de 10% é R$ {sal + (sal * (10 / 100))}')

