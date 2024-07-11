# Ex091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
import operator
from time import sleep
jogadores = {}
print('Valores sorteados: ')
for número in range(4):
    jogadores[f'Jogador {número+1}'] = resultado = randint(1,10) # Adicionando no dicionario a chave = resultado <- sendo gerado pelo = randint. 
    print(f'O {número+1}º Jogador tirou: {resultado} ')
    sleep(1)
jogadores_ordenados = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True) # ordenando para jogadores_ordenados o dicionario pelo metodo operator, utilizando como comparação os valores(values) = item.getter(1), em ordem decrescente.
print('Ranking dos jogadores: ')
for contador,jogador in enumerate(jogadores_ordenados):
    print(f'{contador+1}º lugar: {jogador[0]} com {jogador[1]}')
    sleep(1)

# Resolução do Professor:
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)}
raking= list()
print('Vaklores sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
raking = sorted(jogo.item(), key=itemgetter(1), reverse=True)
print('-='*30)
print('     == Raking dos Jogadores ==')
for i,v in enumerate(raking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
