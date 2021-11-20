"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""


from time import sleep


def contador(x, y, z):
    espera()
    print(f'Contagem de {x} a {y} de {z} em {z}:')
    espera()
    if z == 0:
        z = 1
    if x > y:
        if z > 0:
            for c in range(x, y - 1, -z):
                print(c, end=' ')
                sleep(0.3)
        elif z < 0:
            for c in range(x, y - 1, z):
                print(c, end=' ')
                sleep(0.3)
    elif x < y:
        if z < 0:
            z *= -1
        for c in range(x, y + 1, z):
            print(c, end=' ')
            sleep(0.3)
    pulalinha()
    pulalinha()


def pulalinha():
    print()


def espera():
    sleep(0.5)


contador(1, 10, 1)
contador(10, 0, 2)
espera()
print(f'Sua vez de personalizar a contagem')
inicio = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
pulalinha()
contador(inicio, final, passo)
