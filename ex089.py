"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente."""

diario = []
aluno = []
resp = 'S'
while resp in 'Ss':
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota da A1: '))
    n2 = float(input('Nota da A2: '))
    resp = str(input('Quer continuar? [S/N] '))
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    diario.append(aluno[:])
    aluno.clear()
    while resp not in 'SsNn':
        resp = str(input('Inválido. Responda com S ou N. Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        print('=-' * 20)
        break
print(f"{'Nº':<4}{'NOME':<10}{'MÉDIA':>10}")
for l in range(len(diario)):
    print(f"{l + 1:<3}", end=' ')
    for c in range(1):
        print(f"{diario[l][0]:10}", end=' ')
        print(f"{(diario[l][1] + diario[l][2]) / 2:>8.1f}", end=' ')
    print()
while True:
    print( '=-' * 20 )
    opcao = int(input('Para ver as notas, digite o nº do aluno: (999 para interromper) '))
    if opcao == 999:
        break
    if opcao <= len(diario):
        print(f"{diario[opcao - 1][0]} -> N1: {diario[opcao - 1][1]} | N2: {diario[opcao - 1][2]} ")
print('=-' * 20)
print('Fim')

