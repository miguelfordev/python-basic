# Ex109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from pct109.moeda import *

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preço,True)} é: {moeda(metade(preço), True)}')
print(f'O dobro de {moeda(preço,True)} é: {moeda(dobro(preço),True)}')
print(f'Aumentando 10%, temos: {moeda(aumentar(preço,10),True)}')
print(f'Reduzindo 13%, temos {moeda(diminuir(preço,13),True)}')