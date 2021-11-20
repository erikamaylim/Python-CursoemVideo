from ex115.lib.arquivo import criarArquivo
from uteis.cores import RED, END
from ex115.lib.interface import menu, titulo, leiaInt
from ex115.lib.arquivo import criarArquivo, arquivo, lerArquivo, cadastrar

arq = 'cursoemvideo.txt'

if not arquivo(arq):
    criarArquivo(arq)

while True:
    menu()
    print()
    opcao = int(input('Digite código da opção: '))
    if opcao == 1:
        lerArquivo(arq)
    elif opcao == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        titulo('EXECUÇÃO FINALIZADA')
        break
    else:
        print(f'{RED}OPÇÃO INVÁLIDA! Tente novamente.{END}')
        print()
