# Aula 7
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print('A soma dos números {} e {} é igual a {}.'.format(n1, n2, s), end=' ')
# end='' serve para não pular linha. Para pular, utiliza-se o /n
print('A subtração é {}, a multiplicação é {}, a divisão é {:.2f}'.format(sub, m, d), end=' >>> ')
# No end='' anterior, só inclui >>> para mostarr que pode ter conteúdo dentro das aspas e que ele aparece
print('A divisão inteira é {}, o resto da divisão é {}, um elevado ao outro é {}'.format(di, r, e))


