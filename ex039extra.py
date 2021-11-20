from datetime import date
print('***** ALISTAMENTO MILITAR *****')

sexo = int(input("""Qual o seu sexo? Digite:
1 para Feminino
2 para Masculino
Digite a opção escolhida: """))
if sexo != 1 and sexo != 2:
    print('Opção inválida!')
elif sexo == 1:
    print('O alistamento militar não é obrigatório para mulheres.')
elif sexo == 2:
    ano = int( input( 'Digite seu ano de nascimento: ' ))
    idade = date.today().year - ano
    if idade < 18:
        print(f'Você ainda não tem 18 anos e ainda vai se alistar ao serviço militar em {ano + 18}. Falta(m) {18 - idade} anos.' )
    elif idade == 18:
        print(f'Você tem 18 anos e deve se alistar às forças armadas imediatamente.')
    elif idade > 18:
        print(f'''Você tem mais de 18 anos. Seu ano de alistamente ao serviço militar foi {ano + 18}, à {idade - 18} ano(s).''')
print('Fim')
