"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('******** BANCO PANTINI ********')
valorasacar = int(input('Valor a sacar: R$ '))
céd = 50
valorabatido = valorasacar
qntdcéd = 0
while True:
    if valorabatido >= céd:
        valorabatido -= céd
        qntdcéd += 1
    else:
        if qntdcéd > 0:
            print(f'{qntdcéd} nota(s) de R$ {céd:.2f}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        qntdcéd = 0
        if valorabatido == 0:
            break
print('Saque efetuado com sucesso. VOLTE SEMPRE!')

