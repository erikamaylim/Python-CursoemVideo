from uteis import moeda


valor = float(input('Digite o valor: R$ '))
print(f'Aumentando 10% de {moeda.dinheiro(valor)}, temos {moeda.aumentar(valor, True)}')
print(f'Diminuindo 13% de {moeda.dinheiro(valor)}, temos {moeda.diminuir(valor, True)}')
print(f'A metade de {moeda.dinheiro(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.dinheiro(valor)} é {moeda.dobro(valor, True)}')

