'''             Condicoes Parte 1: Aula
----------------------------------------------------------

ano = int(input('Digite o ano do carro: ))
print('carro novo' if ano <=3 else 'carrovelho)
print('fim')
'''

''' Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
O programa devera escrever na tela se o usuario venceu ou perdeu.
'''

from random import randint
from time import sleep
pc = randint(0,5)
escolha = int(input('Digite o numero que o computador pensou: '))
print('Processando...')
sleep(3)
if pc == escolha:
    print('Voce acertou.')
else:
    print('Voce errou.')
