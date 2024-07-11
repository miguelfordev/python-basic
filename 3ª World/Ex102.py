# Ex102: Crie uma programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrada ou não na tela o processo de cálculo do fatorial.

def fatorial(n,show=False):
    """-> Calcula o Fatorial de um número.
    
    Argumentos
    ----------
    n : int
        Recebe um número para calcular o fatorial.

    show : bool
        Retorne a operação que foi realizada.

    Returns
    -------
    tuple
        Retorne uma tupla, com resultados do fatorial e/ou operação como foi feita.
    """
    if show == True:
        resultado = 1
        for c in range(n, 0, -1):
            resultado *= c
            print(f'{c}', end=' x ' if c != 1 else ' = ')
    else:
        resultado = 1
        for c in range(n, 0, -1):
            resultado *= c
    return resultado


print(fatorial(5,True))
help(fatorial)

# Resolução do Professor:
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5,show=True))
help(fatorial)