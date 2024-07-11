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
    retorno = (p/2)
    return (f'{retorno:.2f}')

def dobro(p=float) -> float:
    retorno = (p*2)
    return (f'{retorno:.2f}')

def aumentar(p=float, porcento=int) -> float:
    retorno = (p+(p/100*porcento))
    return (f'{retorno:.2f}')

def diminuir(p=float, porcento=int) -> float:
    retorno = (p-(p/100*porcento))
    return (f'{retorno:.2f}')

def tela():
    print('-'*25)
    print('     RESUMO DO VALOR')
    print('-'*25)

def resumo(valor, porcento1, porcento2, formatado=False):
    tela()
    valorF = (f'{valor:.2f}')
    print(f'Preço analisado:   {moeda(valorF,formatado)}')
    print(f'Dobro do preço:    {moeda(dobro(valor),formatado)}')
    print(f'Metade do preço:   {moeda(metade(valor),formatado)}')
    print(f'{porcento1}% de aumento:    {moeda(aumentar(valor,porcento1),formatado)}')
    print(f'{porcento2}% de redução:    {moeda(diminuir(valor,porcento2),formatado)}')
