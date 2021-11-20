def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERRO! Valor inválido.')
        else:
            valido = True
            return float(entrada)



