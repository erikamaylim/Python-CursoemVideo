"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = str(input('Informe seu sexo [M/F]: ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção inválida. Por favor, informe seu sexo: ')).strip()[0]
print(f'Sexo {sexo.upper()} cadastrado com sucesso!')