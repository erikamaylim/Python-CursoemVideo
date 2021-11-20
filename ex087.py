"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
somapares = 0
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um nº para a posição {[l, c]}: '))
        if m[l][c] % 2 == 0:
            somapares += m[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{m[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {somapares};')
print(f'A soma dos valores da 3ª coluna é {m[0][2] + m[1][2] + m[2][2]};')
print(f'O maior valor da 2º linha é {max(m[1])}.')
