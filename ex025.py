"""Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome."""

nome = str(input('Digite seu nome completo: ')).lower()
print('O nome digitado possui a palavra SILVA?','silva' in nome)
print('Se a resposta for True, então tem. Se for False, então não tem.')