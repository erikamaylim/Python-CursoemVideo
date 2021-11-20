"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

lista = ('Erika', 'Patricia', 'Hugo', 'Lau', 'Carlos', 'Suki')
for c in lista:
    print(f'\nNa palavra {c.upper( )} temos a(s) vogal(is):', end =' ')
    for caractere in c:
        if caractere.lower() in 'aeiou':
            print(caractere.lower(), end=' ')


