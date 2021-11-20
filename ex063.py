"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela
os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8"""

print('******** SEQUÊNCIA DE FIBONACCI ********')
n = int(input('Quantos termos da Sequência de Fibonacci deseja ver? '))
a, b, c = 0 , 1, 0
print(f'{a} ⇾ {b}', end='')
cont = 3 #Já estou exibindo os 2 primeiros números. Contador não precisa começar do 1
while cont <= n:
    c = a + b
    print(f' ⇾ {c}', end='')
    a = b
    b = c
    cont += 1

