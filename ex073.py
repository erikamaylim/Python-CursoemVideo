"""Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o Flamengo."""

print('***** TABELA DO BRASILEIRÃO *****')
time = ('Bragantino', 'Bahia', 'Ceará', 'Fortaleza', 'Athletico-PR',
        'Flamengo', 'Atlético-GO', 'Cuiabá', 'Sport', 'Juventude',
        'Internacional', 'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG',
        'América-MG', 'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos')
print('=-' * 15)
print(f'Os cinco primeiros colocados: {time[0:5]}')
print('=-' * 15)
print(f'Os quatro últimos colocados: {time[-4:]}')
print('=-' * 15)
print(f'Times em ordem alfabética: {sorted(time)}')
print('=-' * 15)
print(f'Posição do Flamengo na tabela: {time.index("Flamengo") + 1}º lugar')

