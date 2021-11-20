"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

num = list()
n1 = int(input('Digite um nº: '))
num.insert(0, n1)
print('Adicionado ao final da lista')
n2 = int(input('Digite um nº: '))
if n2 > n1:
    num.insert(1, n2)
    print('Adicionado na posição 1')
elif n2 < n1:
    num.insert(0, n2)
    print('Adicionado na posição 0')
n3 = int(input('Digite um nº: '))
if n3 > num[1]:
    num.insert(2, n3)
    print('Adicionado na posição 2')
elif n3 < num[0]:
    num.insert(0, n3)
    print('Adicionado na posição 0')
elif num[0] < n3 < num[1]:
    num.insert(1, n3)
    print('Adicionado na posição 1')
n4 = int(input('Digite um nº: '))
if n4 < num[0]:
    num.insert(0, n4)
    print('Adicionado na posição 0')
elif n4 > num[2]:
    num.insert(3, n4)
    print('Adicionado na posição 3')
elif num[0] < n4 < num[1]:
    num.insert(1, n4)
    print('Adicionado na posição 1')
elif num[1] < n4 < num[2]:
    num.insert(2, n4)
    print('Adicionado na posição 2')
n5 = int(input('Digite um nº: '))
if n5 < num[0]:
    num.insert(0, n5)
    print('Adicionado na posição 0')
elif num[0] < n5 < num[1]:
    num.insert(1, n5)
    print( 'Adicionado na posição 1' )
elif num[1] < n5 < num[2]:
    num.insert(2, n5)
    print( 'Adicionado na posição 2' )
elif num[2] < n5 < num[3]:
    num.insert(3, n5)
    print( 'Adicionado na posição 3' )
elif n5 > num[3]:
    num.insert(4, n5)
    print( 'Adicionado na posição 4' )
print(f'Valor digitados em ordem crescente: {num}')
