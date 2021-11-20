"""Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""

"""for cont in range(1, 50+1): #Range sempre desconsidera o último. Poderia ter colocado 51 ao invés de 50+1.
    print( '.', end=' ' ) #Esse print é para mostrar quantas vezes o laço foi feito.
    if cont % 2 == 0:
        print(cont, end=' ') #Esse end serve para mostrar os números na horizontal."""

"""A solução acima usa mais o processador. A solução de baixo reduz o trabalho dele e dá o mesmo resultado:"""
for num in range(2, 51, 2):
    print(num, end=' ')
"""Um bom programador tenta ao máximo reduzir a carga de trabalho do computador."""