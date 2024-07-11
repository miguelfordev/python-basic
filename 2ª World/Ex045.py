''' Desafio 45: Crie um programa que faca o computador jogar Jokenpo com voce.
        PEDRA PAPEL E TESOURA
'''
from random import sample, choice
from time import sleep
jogo = ['pedra','papel','tesoura']
res = str(input('Digite pedra papel ou tesoura: ')).lower()
pc = choice(jogo)
sleep(2)
print(f'Eu, O PC escolherei...: {pc}')
sleep(2)
if pc == 'pedra' and res == 'tesoura' or pc == 'papel' and res == 'pedra' or pc == 'tesoura' and res == 'papel':
    print(f'O PC ganhou')
elif pc == 'pedra' and res == 'papel' or pc == 'papel' and res == 'tesoura' or pc == 'tesoura' and res == 'pedra':
    print('Voce ganhou!')
elif pc == res:
    print('Deu empate')
else:
    print('Repita o programa, digitou algo errado.')