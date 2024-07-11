'''         Modularização em Python - Módulos e Pacotes
---------------------------------------------------------------------------
Ex:
# Funções: <------------------------------------- VAI PRA OUTRO ARQUIVO CHAMADO: uteis.py
def fatorial(n):
    f=1
    for c in range(1,n+1):
        f*=c
    return f

def dobro(n):
    return n*2

def triplo(n):
    return n*3

# Programa Principal:
import uteis <-------- MANEIRA MAIS RECOMENDADA PARA EVITAR CONFLITOS DE TER FUNÇÕES COM MESMO NOME
num=int(input('Digite um valor: '))
fat=uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
--------------------------------------------------------------------------
Pacote(pasta) uteis: <- Pasta separando os módulos por assunto.
    __init__.py
    - Pasta números:
        __init__.py
        funções.py
    - Pasta strings:
        funções.py
    - Pasta Datas:
        funções.py
    - Pasta Cores:
        funções.py
'''

# Ex107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
from pct107 import moedas

preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é: {moedas.metade(preço)}')
print(f'O dobro de {preço} é: {moedas.dobro(preço)}')
print(f'Aumentando 10%, temos: {moedas.aumentar(preço,10)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(preço,13)}')