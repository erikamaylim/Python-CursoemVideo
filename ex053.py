"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase = str(input('Digite uma frase (sem pontuação ou acento): ')).strip().upper().replace(' ', '')
inverso = frase[::-1].replace(' ', '')
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase NÃO é um palíndromo.')
