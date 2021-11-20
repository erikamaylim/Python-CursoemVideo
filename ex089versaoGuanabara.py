diario = []
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    diario.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp not in 'SsNn':
        resp = str(input('Inválido. Responda com S ou N. Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        print('=-' * 25)
        break
print(f"{'Nº':<4}{'NOME':<10}{'MEDIA':>10}{'STATUS':>16}")
for i, n in enumerate(diario):
    print(f"{i + 1:<4}{n[0]:<10}{n[2]:>9.1f}", end='')
    if n[2] >= 6:
        print(f"{'APROVADO':>18}")
    elif n[2] >= 4:
        print(f"{'RECUPERAÇÃO':>20}")
    else:
        print(f"{'REPROVADO':>19}")
while True:
    print('=-' * 25)
    opcao = int(input('Para ver as notas, digite o nº do aluno (nº negativo interrompe): '))
    if opcao < 0:
        break
    if opcao <= len(diario):
        print(f"{diario[opcao - 1][0]} -> Notas: {diario[opcao - 1][1]}")
print('FIM')
