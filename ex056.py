"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- a média de idade do grupo;
- qual é o nome do homem mais velho;
= quantas mulheres têm menos de 20 anos."""

somaidade = 0
mulhermenor20 = 0
idadehomemvelho = 0
nomehomemvelho = ''
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()

    somaidade += idade

    if sexo in 'Mm' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome

    if sexo in 'Ff' and idade < 20:
        mulhermenor20 += 1

print(f'A média de idade do grupo é {(somaidade / 4):.1f}.')
print(f'O homem mais velho se chama {nomehomemvelho} e ele tem {idadehomemvelho} anos.')
print(f'Há {mulhermenor20} mulheres com menos de 20 anos.')

