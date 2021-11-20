"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

valor = float(input('Valor da compra: R$ '))
forma = int(input('''Forma de Pagamento:
[1] Dinheiro
[2] Cheque
[3] Cartão
Digite o nº da opção desejada: '''))
vezes = int(input('Em quantas vezes vai pagar? (Se for à vista, digite 1) '))

if (forma == 1 and vezes == 1) or (forma == 2 and vezes == 1):
    print(f' No dinheiro ou cheque à vista você tem 10% de desconto.\nO valor a pagar é R$ {valor - (valor * (10 / 100)):.2f}.')
elif forma == 3 and vezes == 1:
    print(f'No cartão à vista você tem 5% de desconto. O valor a pagar é R$ {valor - (valor * (5 / 100)):.2f}')
elif forma == 3 and vezes <= 2:
    print(f'No cartão em até 2x não há desconto. O valor a pagar é R$ {valor:.2f}.')
elif forma == 3 and vezes >= 3:
    print(f'Pagamentos no cartão com 3 ou mais parcelas têm 20% de juros.')
    print(f'''Sua compra será parcelada em {vezes}x de R$ {(valor + (valor * (20 / 100))) / vezes:.2f}. Total R$ {valor + (valor * (20 / 100)):.2f}.''')
else:
    print('Opção inválida')
