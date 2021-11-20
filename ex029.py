"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima  do limite."""

v = float(input('A quantos quilômetros por hora você estava? '))
if v > 80:
    print('Você foi multado!')
    print(f'O valor da multa é R${(int(v) - 80) * 7:.2f}.' )
else:
    print('Tudo em ordem. Tenha uma boa viagem e continue dirigindo com segurança.')