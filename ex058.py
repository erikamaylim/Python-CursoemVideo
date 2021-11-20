"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer."""

from random import randint
num = randint(0, 10)
print('''Pensei em um número de 0 a 10.
Você consegue adivinhar?''')
palpite = int(input('Qual número eu pensei? '))
tentativas = 1
while palpite != num:
    tentativas +=1
    if palpite < num:
        palpite = int(input('Mais que isso. Tente de novo: '))
    elif palpite > num:
        palpite = int(input('Menos que isso. Tente de novo: '))
if palpite != num:
    tentativas += 1
if palpite == num:
    if tentativas > 5:
        print(f'Demorou, mas ACERTOU! Você precisou de {tentativas} tentativas para acertar o nº {num}. Tente melhorar!')
    elif tentativas <= 5 and tentativas != 1:
        print(f'Muito bem! Com {tentativas} tentativa(s) você acertou o nº {num}. Parabéns!')
    elif tentativas == 1:
        print(f'QUE RÁPIDO! Só precisou de 1 tentativa para acertar o nº {num}! Excelente!')
