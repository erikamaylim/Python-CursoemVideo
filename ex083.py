"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com
os parênteses abertos e fechados na ordem correta."""

e = str(input('Digite uma expressão: '))
paren = []
for simb in e:
    if simb == "(":
        paren.append('(')
    elif simb == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break
print(paren)
if len(paren) == 0:
    print('Sua expressão é válida!')
else:
    print('ERRO! Sua expressão é INVÁLIDA!')