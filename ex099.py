"""Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


from time import sleep


def maior(* val):
    print('Analisando os valores passados...')
    for c in val:
        print(c, end=' ')
        sleep(0.5)
    if len(val) != 0:
        sleep(0.5)
        print(f"| Foram informados {len(val)} valores")
        sleep(0.5)
        print(f"O maior valor informado foi {max(val)}.")
    else:
        print("Nao foi informado nenhum valor !")
    print()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

