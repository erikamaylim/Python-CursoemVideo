"""Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""

time = []
jogador = {}
gols = []
while True:
    jogador['Nome'] = str(input('Nome: ')).strip().title()
    jogador['Partidas'] = int(input('Partidas: '))
    for c in range(jogador['Partidas']):
        gols.append(int(input(f'   Qntd gols da {c+1}ª partida: ')))
    jogador['Gols'] = gols[:]
    jogador['Total de gols'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp not in 'SsNn':
        resp = str(input('OPÇÃO INVÁLIDA! Apenas S ou N.\nQuer continuar? [S/N]: ')).strip()[0]
    elif resp in 'Nn':
        break
print()
print(f'{"Cod":<6}{"Nome":16}{"Gols":<20}{"Total":>20}')
for i, t in enumerate(time):
    print(f"{i + 1:<5} {t['Nome']:<15} {str(t['Gols']):<30} {t['Total de gols']:>9}")
print()
while True:
    qual = int( input( 'Quer ver os dados de qual jogador? (Nº negativo para parar): '))
    if qual > len(time) or qual == 0:
        qual = int(input('INVÁLIDO.\nQuer ver os dados de qual jogador? (Nº negativo para parar): '))
    print()
    if 0 < qual <= len(time):
        print(f'--- LEVANTAMENTO DO JOGADOR {time[qual - 1]["Nome"].upper()} ---')
        for i, v in enumerate(time[qual - 1]['Gols']):
            print(f'      > {i + 1}ª partida: {v} gol(s)')
        print()
    else:
        break
print('FIM')

