# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.

from random import randint
from time import sleep
pc = randint(0,10)
tentativas =1
escolha = int(input('Digite um numero de 1 a 10 que o computador pensou: '))
while True:
    print('Processando...')
    sleep(0.7)
    if escolha > pc:
        print('O numero é menor.',end='')
        escolha = int(input('Tentativa errada. Tente mais uma vez: '))
        tentativas += 1
    if escolha < pc:
        print('O numero é maior.',end='')
        escolha = int(input('Tentativa errada. Tente mais uma vez: '))
        tentativas += 1
    if pc == escolha:
        print(f'Voce acertou. Com {tentativas} tentativas. O pc escolheu o numero: {pc}')
        break