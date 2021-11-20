"""Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’)
Saída: ~~~~~~~~~~~~
        Olá, Mundo!
       ~~~~~~~~~~~~
"""


def escreva(txt):
    print(f'~' * (len(frase) + 4))
    print(f"  {txt.upper()}")
    print(f'~' * (len(frase) + 4))


frase = str(input('Digite uma frase qualquer: ')).strip()


escreva(frase)

