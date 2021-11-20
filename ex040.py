"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO"""

n1 = float(input('Digite a nota da A1: '))
n2 = float(input('Digite a nota da A2: '))
m = (n1 + n2) / 2
RED = "\033[1;31m"
END = "\033[0m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;93m"
if m < 5:
    print(f'Sua média foi {m:.1f}. Você está {RED}REPROVADO{END}')
elif 7 > m >= 5:
    print(f'Sua média foi {m:.1f}. Você está de {YELLOW}RECUPERAÇÃO{END}')
elif m >= 7:
    print(f'Sua média foi {m:.1f}. Você está {GREEN}APROVADO{END}')
