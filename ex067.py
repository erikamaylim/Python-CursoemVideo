"""Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

print('******** TABUADA ********')
while True:
    n = int(input('Ver tabuada do nº: '))
    print( '-' * 20 )
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n * c:3}')
    print('-' * 20)
    print('[Para parar, digite um nº negativo]')
print('Programa interrompido.')
