def leiaDin(msg):
    while True:
        preço = input(msg)
        for letra in preço:
            if letra == ',':
                preço = preço.replace(',','.')
        try:
            novoFormato = float(preço)
            break
        except:
            print('Valor inválido.')
    return novoFormato
    