"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

mais18 = homens = mulherjovem = 0
while True:
    print('======== CADASTRE UMA PESSOA ========')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FfMm':
        sexo = str(input( 'Sexo [M/F]: ')).strip()[0]
    if idade >= 18 :
        mais18 += 1
    if sexo in "Mm" :
        homens += 1
    if sexo in "Ff" and idade < 20:
        mulherjovem += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        print('Execução interrompida.')
        print('=-' * 15)
        break
print( f'Total de pessoas com 18 anos ou mais: {mais18}.')
print( f'Total de pessoas do sexo masculino: {homens}.')
print( f'Total de mulheres com menos de 20 anos: {mulherjovem}.')
