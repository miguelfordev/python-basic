'''         Aula 21 - Funções Parte 2
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Interactive Help:
    - help() - dá uma descrição sobre algum metodo que voce tem interesse em pesquisar.
    - print(input.__doc__)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Docstrings:
    def contador(i,f,p):
        """ Isso é uma docstrings. Documentação de como funciona a função.
        -> Faz uma contagem e mostra na tela.
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
        """
        c=i
        while c<=f:
            print(f'{c}',end='..')
            c+=p
        print('FIM!')

help(contador)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
Parâmetros Opcionais:
    def somar(a,b,c=0):
        """ c <- parâmetro opcional. Assumindo um valor padrão para função.
        """
        s=a+b+c
        print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Escopo de variáveis:
    def teste():
    glogal k <- força a função a usar a variavel global (k=5) ao inves da local (k=0) ou seja vai utilizar k no programa principal vai valer 0 (k=0). global <- palavra reservada
    k=0
    x=8
        print(f'Na função teste, n vale {n}') <- Imprimi
        print(f'Na função teste, x vale {x}') <- Imprimi

    # Programa Principal:
        n=2
        k=5
        print(f'No programa principal, n vale {n}') <- Imprimi - Escopo global, funciona tanto na função quanto no programa principal.
        print(f'No programa principal, x vale {x}') <- Não imprimi - Vai dar erro no programa, por que x é escopo local.
        teste()
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Retorno de valores:
    - return: retorna resultados.

    Exemplo:
    def somar(a=0,b=0,c=0):
        s=a+b+c
        return s

    r1=somar(3,2,5)
    r2=somar(1,7)
    r3=somar(4)
    print(f'Meus cálculos deram {r1},{r2} e {r3}.')
'''

# Ex101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.

def voto(anoN):
    from datetime import datetime
    anoA = datetime.today().year
    idade = anoA - anoN
    if idade < 18:
        situacao = 'Não vota.'
    elif idade >= 18 and idade < 65:
        situacao = 'Voto obrigatório.'
    else:
        situacao = 'Voto opcional.'
    return idade,situacao


anoDeNascimento = int(input('Digite o seu ano de nascimento: '))
idade, situacaoVoto = voto(anoDeNascimento)
print(f'{idade} anos. Situação: {situacaoVoto}')

# Resolução do Professor:
def voto(ano):
    from datetime import date 
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    

# Programa Principal
nasc = int(input('Em que ano você nasceu? '))   
print(voto(nasc))