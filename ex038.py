"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
CYANO = "\033[1;36m"
END = "\033[0m"
YELLOW = "\033[1;93m"
if n1 > n2:
    print(f'O primeiro nº digitado, {YELLOW}{n1}{END}, é {CYANO}MAIOR{END} que o segundo nº, {YELLOW}{n2}{END}.')
elif n2 > n1:
    print(f'O primeiro nº digitado, {YELLOW}{n1}{END}, é {CYANO}MENOR{END} que o segundo nº, {YELLOW}{n2}{END}.')
else:
    print(f'Os dois números digitados são {CYANO}IGUAIS{END}.')
