"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

jogador = {}
gols = []
jogador['Nome'] = str(input('Nome: ')).strip()
jogador['Partidas'] = int(input('Partidas: '))
for c in range(jogador['Partidas']):
    gols.append(int(input(f'Qntd gols da {c+1}ª partida: ')))
jogador['Gols'] = gols[:]
jogador['Total de gols'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for i, v in enumerate(gols):
    print(f'Na {i+1}ª partida, fez {v} gols')
print(f'Total de {jogador["Total de gols"]} gols')

