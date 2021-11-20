"""Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores."""
from uteis import cores


def ajuda():
    while True:
        print(f'{cores.BACK_BLUE} SISTEMA DE AJUDA PyHELP {cores.END}')
        comando = str(input(f'{cores.BACK_DARK_GREY} Função ou Biblioteca ("fim" para sair) >{cores.END} ').strip())
        if comando.lower() == 'fim':
            break
        else:
            help(comando)
    print(f'\n{cores.BACK_RED} FINALIZADO {cores.END}')


ajuda()
