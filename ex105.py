"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
- A maior nota
– A menor nota
– A média da turma
– A situação (opcional)"""


def notas(* num, s=False):
    """
    -> Função para coletar notas dos alunos e retornar informações gerais e a situação da turma.
    :param num: Notas da turma
    :param s: Situação (Boa, Razoável ou Ruim)
    :return: dicionário com informações sobre a turma
    """
    soma = sum(num)
    qtd = len(num)
    maior = max(num)
    menor = min(num)
    media = soma / qtd
    if media >= 6:
        sit = 'Boa'
    elif media >= 5:
        sit = 'Razoável'
    else:
        sit = 'Ruim'
    total = {'Quantidade de notas': qtd, 'Maior nota': maior, 'Menor nota': menor, 'Média': media}
    if s:
        total['Situação'] = sit
    return total


print(notas(2, 3, 5, 4, 1, 3, s=True))
print(notas(10, 7, 8, 10, s=True))
print(notas(4, 6, 7, 5, 6.5, 7, 5))
help(notas)
