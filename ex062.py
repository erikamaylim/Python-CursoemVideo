"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

print('##### PROGRESSÃO ARITMÉTICA #####')
num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{num} ⇾ ', end=' ')
        num += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quer ver mais quantos termos dessa PA? '))
print(f'O programa foi finalizado após exibir {total} termos.')