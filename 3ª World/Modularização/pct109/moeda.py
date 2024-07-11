def moeda(valor,formatado=False):
    if formatado == True:
        novoFormato = (f'R${valor}')
    else:
        novoFormato = valor
    return novoFormato

def metade(p=float) -> float:
    '''Função que retorna metade de uma variável do tipo float.
    
    param: p type float:
        aceita um parâmetro númerico de tipo ponto flutuante.
    return: 
        retorna metade do valor.
    '''
    return (p/2)

def dobro(p=float) -> float:
    return (p*2)

def aumentar(p=float, porcento=int) -> float:
    return (p+(p/100*porcento))

def diminuir(p=float, porcento=int) -> float:
    return (p-(p/100*porcento))